// Self-checking Icarus Verilog testbench for one UART frame.
`timescale 1ns/1ps
module tb_uart_tx;
    reg clk = 0;
    always #5 clk = ~clk;
    reg rst = 1, start = 0;
    reg [7:0] data = 8'hA5;
    wire tx, busy, done;
    localparam B = 8;
    uart_tx #(.CLKS_PER_BIT(B)) dut(
        .clk(clk), .rst(rst), .start(start), .data(data),
        .tx(tx), .busy(busy), .done(done)
    );
    integer i;
    initial begin
        repeat(3) @(negedge clk);
        rst = 0;
        @(negedge clk);
        start = 1;
        @(negedge clk);
        start = 0;
        // Sample each bit in its middle, beginning with start.
        repeat(B/2 - 1) @(negedge clk);
        if (tx !== 0) $fatal(1, "missing start bit");
        repeat(B) @(negedge clk);
        for (i = 0; i < 8; i = i + 1) begin
            if (tx !== data[i]) $fatal(1, "incorrect data bit %0d", i);
            repeat(B) @(negedge clk);
        end
        if (tx !== 1) $fatal(1, "missing stop bit");
        repeat(B) @(negedge clk);
        if (busy !== 0 || done !== 1) $fatal(1, "done/busy mismatch");
        $display("PASS: UART sent 8'h%02h", data);
        $finish;
    end
endmodule

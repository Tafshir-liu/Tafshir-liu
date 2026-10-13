// Simple 8-N-1 UART transmitter, Verilog-2001.
// CLKS_PER_BIT must be >= 2. One-cycle done pulse after stop bit.
module uart_tx #(
    parameter integer CLKS_PER_BIT = 16
)(
    input wire clk,
    input wire rst,
    input wire start,
    input wire [7:0] data,
    output reg tx,
    output reg busy,
    output reg done
);
    localparam IDLE = 2'd0, START = 2'd1, DATA = 2'd2, STOP = 2'd3;
    reg [1:0] state;
    integer count;
    reg [2:0] bit_index;
    reg [7:0] data_latched;
    always @(posedge clk) begin
        if (rst) begin
            tx <= 1'b1;
            busy <= 1'b0;
            done <= 1'b0;
            count <= 0;
            bit_index <= 0;
            data_latched <= 0;
            state <= IDLE;
        end else begin
            done <= 1'b0;
            case (state)
                IDLE: begin
                    tx <= 1'b1;
                    busy <= 1'b0;
                    count <= 0;
                    if (start) begin
                        data_latched <= data;
                        busy <= 1'b1;
                        tx <= 1'b0;
                        state <= START;
                    end
                end
                START: begin
                    if (count == CLKS_PER_BIT - 1) begin
                        count <= 0;
                        tx <= data_latched[0];
                        bit_index <= 0;
                        state <= DATA;
                    end else count <= count + 1;
                end
                DATA: begin
                    if (count == CLKS_PER_BIT - 1) begin
                        count <= 0;
                        if (bit_index == 7) begin
                            tx <= 1'b1;
                            state <= STOP;
                        end else begin
                            bit_index <= bit_index + 1'b1;
                            tx <= data_latched[bit_index + 1'b1];
                        end
                    end else count <= count + 1;
                end
                STOP: begin
                    if (count == CLKS_PER_BIT - 1) begin
                        count <= 0;
                        state <= IDLE;
                        busy <= 1'b0;
                        done <= 1'b1;
                    end else count <= count + 1;
                end
                default: state <= IDLE;
            endcase
        end
    end
endmodule

`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer: 
// 
// Create Date: 05/19/2019 12:01:11 PM
// Design Name: 
// Module Name: Controller
// Project Name: 
// Target Devices: 
// Tool Versions: 
// Description: 
// 
// Dependencies: 
// 
// Revision:
// Revision 0.01 - File Created
// Additional Comments:
// 
//////////////////////////////////////////////////////////////////////////////////


module Controller(
    input               clk,
    input               rst_n,
    input       [7:0]   WReg,
    output  reg [7:0]   RReg_Switch,    
    output  reg [7:0]   RReg_Button,
    input       [7:0]   SW,
    input       [7:0]   BUTTON,
    output      [7:0]   LED
    );
    always  @(posedge clk) begin
        if(!rst_n) begin
            RReg_Switch <= 8'h0;
            RReg_Button <= 8'h0;
        end
        else begin
            RReg_Switch <= SW;
            RReg_Button <= BUTTON;
        end
    end
    assign LED = WReg;
endmodule

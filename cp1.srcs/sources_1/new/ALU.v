`timescale 1ns / 1ps


module ALU(num1,num2,opcode,ans);
  input [3:0] num1;
  input [3:0] num2;
  input [1:0] opcode;
  output  reg [3:0]  ans;
  reg [3:0] temp;
  

  always @(*)
  
  begin
     case(opcode)
     2'b00:
     temp=num1+num2;
     2'b10:
     temp=num1|num2;
     2'b01:
     temp=num1&num2;
     2'b11:
     temp=~num1+1;
     endcase
     ans=temp;
  end
   
   
    
    
    
    
       
endmodule
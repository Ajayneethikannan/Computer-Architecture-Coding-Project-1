`timescale 1s / 1ms

module ALU_tb();

     reg clk;
     reg [9:0] mem[0:0];
     reg [9:0] temp;
     wire [3:0] ans;
     wire [6:0] seven;
     integer write_file;
     /* Initial block to generate clock and reset */   
         ALU myAlu(          
              .num1(temp[9:6]),     
              .num2(temp[5:2]),     
              .opcode(temp[1:0]),     
               .ans(ans));

         BdcTo7Seg bcd (
         .bcd(ans),
         .seg(seven)
         );         
     initial 
         begin
        clk = 0;
        temp = 9'b000000000;
        

    
    
      
        forever begin
            #10 clk = !clk;
              $rewind(write_file);
              write_file = $fopen("D:\cp1\output.txt","w");
              $fwrite(write_file,"%b",seven);  
              $fclose(write_file);    
              $readmemb("D:\input.txt", mem);  
              temp  = mem[0];                   
              



 
            end
     end




endmodule

module YALU_tb();

   
    reg [3:0] num1;
    reg [3:0] num2;
    reg [1:0] opcode;
    wire [3:0] ans;
    reg [9:0] mem1 [2:0];
    reg [9:0] mem[0:0];
    reg [9:0] temp;
    reg temp2[3:0];
    
       
      
          
    initial
   
   
      
      begin
      #2  
       $readmemb("D:\input.txt", mem);
           
           
       temp  = mem[0];
           
       $finish;
 
      
     
     
     end
     
     
     
     
     
     
     
     
     
      
   
   
    
    
endmodule
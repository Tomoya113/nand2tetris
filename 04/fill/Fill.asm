(RESET)
    @SCREEN
    D=A
    @address
    M=D

(FILL)
    @KBD
    D=M
    @BLACK
    D;JNE 

(WHITE)
    D=0
    @SET
    0;JMP

(BLACK)
    D=-1

(SET) 
    @address
    A=M
    M=D

    @address
    M=M+1

    @KBD
    D=A
    @address
    D=D-M
    @RESET
    D;JLE

    @FILL
    0;JMP
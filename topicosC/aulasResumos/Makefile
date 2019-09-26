sumdata.o: sumdata.c
    gcc -Wall -Werror -E sumdata.c > sumdata.i
    gcc -Wall -Werror -S sumdata.i
    gcc -Wall -Werror -c sumdata.s

summain.o: summain.c
    gcc -Wall -Werror -E sumdata.c > sumdata.i
    gcc -Wall -Werror -S sumdata.i
    gcc -Wall -Werror -c sumdata.s

sum: sumdata.o summain.o
    gcc -Wall -Werror summain.o sumdata.o -o sun

.PHONY: clean

clean:
	rm *.i *.s *.o sum
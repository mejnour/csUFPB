#define OFFSET_VALUE 10
#define OFFSET_FUNCTION( val ) + OFFSET_VALUE

int main( int argc, char *argv[] ) {
    int x;

    if ( argc > 1 ) 
        x = 2;
    else
        x = 1;
        
    // Aqui dá pau com esses <3 *>
    // O preprocessador avalia a expressão pra
    // 3 * x + 10
    // Como a multiplicação tem precedencia sobre a soma,
    // o resultado da operação é errado
    int y = 3 * OFFSET_FUNCTION( x );
    return y;
}
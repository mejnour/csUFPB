#define OFFSET_VALUE 10
#define OFFSET_FUNCTION( val ) + OFFSET_VALUE

int main( int argc, char *argv[] ) {
    int x;

    if ( argc > 1 ) 
        x = 2;
    else
        x = 1;
        
    int y = OFFSET_FUNCTION( x );
    return y;
}
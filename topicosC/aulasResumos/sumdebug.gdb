set width 0
set height 0
set verbose off

b 8

commands 1
  silent
  printf  "acc = %i\n", acc
  continue
end

b 10

commands 2
  silent
  printf  "acc = %i\n", acc
  continue
end

run

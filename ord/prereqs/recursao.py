def sum_recurs(aux):
    if aux == 5:
        return aux

    aux += 1
    return sum_recurs(aux)


if __name__ == "__main__":
    aux = 0
    while aux < 5:
        aux += 1

    print(aux)
    print(sum_recurs(aux))

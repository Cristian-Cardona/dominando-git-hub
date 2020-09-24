def array_diff(a, b):
    c=a
    cordenadas=[]   # aqui guardo las cordenadas de las ubicaciones de la matriz en a que deben ser borradas
    len_a=len(a)

    for i in range(len_a):
        #print(f'i: {a[i]}')


        for otro in b:
            #print(f"otro: {otro}")

            if otro == a[i]:
                #print(f'if: {otro}')
                cordenadas.append(i)
                #print(f"resultado cordenadas: {cordenadas}")





    for r in cordenadas:
        #print(f"no se donde estoy  {r}")
        c[r]=0

        #print(f'ya borre: {r}')



    return c

a=[]
b=[1, 2]
c=array_diff(a,b)
print(f'C : {c}')

def M_dist():
    x=[]
    y=[]
    b=0
    print 'Informe o numero de pontos'
    n = int(raw_input())
    if(n>0):
        print 'informe as abcissas dos pontos'
        for i in range(1,n+1):
            z=float(raw_input())
            x.append(z)
        print 'informe as ordenadas dos pontos'
        for j in range(1,n+1):
            z=float(raw_input())
            y.append(z)
        for k in range(1,n+1):
            for l in range(1,n+1):
                d=distancia(x[k-1],y[k-1],x[l-1],y[l-1])
                if(d>b):
                    b=d
    return b

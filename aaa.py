def dechiffrer(text):
    tab_de_freq = [['e'], ['a'], ['i'], ['s'], ['t'], ['n'],['r'], ['u'], ['l'], ['o'], ['d'], ['m'],  ['p'], ['q'], ['c'], ['v'], ['b'], ['f'], ['j'], ['j'], ['h'], ['x'], ['z'], ['y'], ['k'], ['w']]
    table = []
    alphabet = "abcdefjhijklmnopqrstuvwxyz"
    esp = 0
    text = text.lower()







    for i in alphabet:
        position = ord(i) - 97
        l = []
        l.append(i)
        table.append(l)

    for caractere in text:

        if caractere == " ":
            esp += 1
            continue

        if caractere == "’":
            esp += 1
            continue

        position = ord(caractere) - 97

        a = int(table[position])
        a += 1




    length = len(text) - esp

    for i in table:
        i[1] = format(int(i[1]) / length)

    table.sort(key=lambda x: x[1])

    i = 0
    k = 0
    taille = 26
    while i < taille:
        k += ord(table[i]) - ord(tab_de_freq[i])
        i += 1

    k = int(k / taille)



    for key in range(k - 1, k + 2):

        message = ""

        for caractere in text:

            if caractere == " ":
                message += " "
                continue

            a = ord(caractere) - key

            if a < 79:

                message += chr(a + 26)

            else:
                message += chr(a)


        print("message clair :")
        print(message)
        print()



print(" le message que vous voulez déchiffrer :u’wkl twsmugmh hdmk vaxxauadw im’ad f’q hsjjsal vw fgetjwmp hjglgugdwk kgfl wpseafwkvsfk dwk hjguzsafk uzshaljwk vsfk uwjlsafk mf vwk hsjlauahsfl hwml ljgehwj dwksmljwk vsfk v’smljwk mf wkhagf hwml sdlwjwj dw hjglgugd gm shhjwfvjw vwk afxgjeslagfkkwujwlwk uwjlsafk hjglgugdwk wuzgmwfl xsmlw vw hjwuakagf vsfk ds vwxafalagf vwk jwyawkv’smljwk wuzgmwfl hsjuw imw dwmjk smlwmjk gfl esfimw vw ewlaumdgkalw vsfk dwmj sfsdqkwugeew hgmj mf sdygjalzew ad wkl tawf hdmk vaxxauadw vw hjgmnwj im’mf hjglgudw wklkmj imw dw ugfljsajw")
msg="u’wkl twsmugmh hdmk vaxxauadw im’ad f’q hsjjsal vw fgetjwmp hjglgugdwk kgfl wpseafwkvsfk dwk hjguzsafk uzshaljwk vsfk uwjlsafk mf vwk hsjlauahsfl hwml ljgehwj dwksmljwk vsfk v’smljwk mf wkhagf hwml sdlwjwj dw hjglgugd gm shhjwfvjw vwk afxgjeslagfkkwujwlwk uwjlsafk hjglgugdwk wuzgmwfl xsmlw vw hjwuakagf vsfk ds vwxafalagf vwk jwyawkv’smljwk wuzgmwfl hsjuw imw dwmjk smlwmjk gfl esfimw vw ewlaumdgkalw vsfk dwmj sfsdqkwugeew hgmj mf sdygjalzew ad wkl tawf hdmk vaxxauadw vw hjgmnwj im’mf hjglgudw wklkmj imw dw ugfljsajw"
dechiffrer(msg)
from gamestorrent import Gamestorrent

gt = Gamestorrent()

search_name = input('Inserisci il nome del gioco da ricercare : ')

print('[/] Starting research ...')
search_found = gt.search(search_name)

count = 0

for search in search_found:
    print('{} : {}'.format(count, search))
    count += 1
    
choosen_game = int(input('Inserisci il numero corrispondente al gioco desiderato : '))

print('Hai scelto di scaricare : ', search_found[choosen_game])

print(gt.get_magnet(search_found[choosen_game]))
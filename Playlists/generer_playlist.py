import os
import random

# ============================================================
#  CONFIGURATION — modifie ces chemins si besoin
# ============================================================
DOSSIER_MUSIQUES  = r"D:\Radio New vegas\Playlists\Musiques"
DOSSIER_BULLETINS = r"D:\Radio New vegas\Playlists\Bulletins"
FICHIER_SORTIE    = r"D:\Radio New vegas\Playlists\RNV.txt"
MUSIQUES_PAR_BULLETIN = 3   # 1 bulletin toutes les X musiques
# ============================================================

def lister_mp3(dossier):
    fichiers = [
        os.path.join(dossier, f)
        for f in os.listdir(dossier)
        if f.lower().endswith(".mp3")
    ]
    return fichiers

musiques  = lister_mp3(DOSSIER_MUSIQUES)
bulletins = lister_mp3(DOSSIER_BULLETINS)

if not musiques:
    print("Aucune musique trouvée dans", DOSSIER_MUSIQUES)
    exit(1)
if not bulletins:
    print("Aucun bulletin trouvé dans", DOSSIER_BULLETINS)
    exit(1)

# Mélange aléatoire
random.shuffle(musiques)
random.shuffle(bulletins)

# Construction de la playlist
playlist = []
bulletin_index = 0

for i, musique in enumerate(musiques):
    playlist.append(musique)

    # Toutes les X musiques, on insère un bulletin
    if (i + 1) % MUSIQUES_PAR_BULLETIN == 0:
        if bulletin_index < len(bulletins):
            playlist.append(bulletins[bulletin_index])
            bulletin_index += 1
        else:
            # On a utilisé tous les bulletins, on recommence depuis le début
            random.shuffle(bulletins)
            bulletin_index = 0
            playlist.append(bulletins[bulletin_index])
            bulletin_index += 1

# Écriture du fichier
with open(FICHIER_SORTIE, "w", encoding="utf-8") as f:
    for piste in playlist:
        f.write(piste + "\n")

print(f"Playlist générée avec succès !")
print(f"  {len(musiques)} musiques")
print(f"  {bulletin_index} bulletins utilisés")
print(f"  {len(playlist)} pistes au total")
print(f"  Fichier : {FICHIER_SORTIE}")

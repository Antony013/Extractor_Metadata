from PIL import Image
from PIL.ExifTags import TAGS
from argparse import ArgumentParser

# description du script
parser = ArgumentParser(
    prog='Extracteur de méta donnée.',
    description='Extrait les méta données et les donées exif (s\'il y en a) d\'une image donné en argument.'
)

# ajouter des arguments au script
parser.add_argument("-img", "--image",
                    help="Nom et format de l'image", type=str)

args = parser.parse_args()

try:
    # récupère le nom de l'image et va chercher le path
    imagename = args.image

    # récupère les données de base de l'image avec PIL - format, heigth, width ...
    image = Image.open(imagename)

    # on extrait les données de base
    info_dict = {
        "Filename": image.filename,
        "Image Size": image.size,
        "Image Height": image.height,
        "Image Width": image.width,
        "Image Format": image.format,
        "Image Mode": image.mode,
        "Image is Animated": getattr(image, "is_animated", False),
        "Frames in Image": getattr(image, "n_frames", 1)
    }

    # on print - le 25 sert juste à mettre de l'espace après le label
    for label, value in info_dict.items():
        print(f"{label:25}: {value}")

    """ EXIF ​​( format de fichier d'image échangeable ) stockent des données importantes sur les photographies. Presque tous les appareils photo numériques créent ces fichiers de données chaque fois que vous prenez une nouvelle photo. """

    # on récupère les données exif avec PIL
    exifdata = image.getexif()

    if len(exifdata) == 0:
        print('\nAucune donnée EXIF à extraire.\n')

    # pour chaque exifdata
    for tag_id in exifdata:
        # on va chercher le nom de la data au lieu de l'id
        tag = TAGS.get(tag_id, tag_id)
        # on récupère le données associé à l'id
        data = exifdata.get(tag_id)
        # si il y a des données en octes alors on les décodes
        if isinstance(data, bytes):
            data = data.decode()
        # on print - le 25 sert juste à mettre de l'espace après le label
        print(f"{tag:25}: {data}")
except:
    print('\nImpossible d\'extraire les données pour cette image.\n\nVérifiez le format et le nom : Le nom ne doit pas comporter d\'espace.\n')

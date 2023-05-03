# Exctraeur de métadonnée

Extrait les méta données et les donées exif (s'il y en a) d'une image donné en argument.

_________________

Options :
  -h, --help, AIDE Afficher l'aide
  -img, --image IMAGE Nom et format de l'image
  
_________________

Exemples :

<code> python extrateur_meta_donnee.py -img image.jpg </code>
> Filename                 : image.jpg
> Image Size               : (4032, 2268)
> Image Height             : 2268
> Image Width              : 4032
> Image Format             : JPEG
> Image Mode               : RGB
> Image is Animated        : False
> Frames in Image          : 1
> ImageWidth               : 4032
> ImageLength              : 2268
> ResolutionUnit           : 2
> ExifOffset               : 226
> Make                     : samsung
> Model                    : SM-G973F
> Software                 : G973FXXSEFUL1
> Orientation              : 6
> DateTime                 : 2023:05:03 10:19:19
> YCbCrPositioning         : 1
> XResolution              : 72.0
> YResolution              : 72.0

<code> python extrateur_meta_donnee.py -img image2.jpg </code>
> Filename                 : image2.jpg
> Image Size               : (200, 133)
> Image Height             : 133
> Image Width              : 200
> Image Format             : JPEG
> Image Mode               : RGB
> Image is Animated        : False
> Frames in Image          : 1
> Copyright                : Eduardo Mariano Rivero

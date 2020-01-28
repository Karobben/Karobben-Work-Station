# Karobben-Work-Station

<a href="#NCBI1">NCBI_GSM.py</a>
<a href="#Imresize">Imresize.py</a> A light image/imges resize python script for resizing one or a group of img.

## <div id="NCBI1">NCBI_GSM.py</div>

NCBI_GSM.py is a scrip for grepping the information from the NCBI database. Since the format per GSE is so different. So you need to change the code to fit your purpose. Since the IP will probably be locked or limited by the NCBI because of frequency requests, I didn't apply the multiprocessing on here. 
```
NCBI_GSM.py -i list -o result.csv
```
## <div id="Imresize">Imresize.py</div>

```
Imresize.py -i input.png  #w=w/2, h=h/2
Imresize.py -i input.png -w #900 #w=900
Imresize.py -i input.png -t #900 #h=900
Imresize.py -i input.png -r 4 #w=w/4, h=h/4
```
You can resize img/imgs by width(-w), by height(-t), by both(-w -t) or by ratio(-r).<br>
You can also read one img each time, with default arguments, output file names as "Re_" + input.png.<br>
You can resize a group of img by using: -i "*.png" (the quotation marks here can not be omitted). The result will be importted to a directory with the same name.<br>
You can also read all imgs form a directory(single directory each). The way output is the same as when you read a bunch of img in a time.

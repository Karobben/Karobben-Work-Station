# Karobben-Work-Station

<a href="#Imresize">Imresize.py</a> A light image/imges resize python script for resizing one or a group of img.<br>
<a href="#Kivy">Kivy_animation_1.py</a> A example of animation in Kivy.<br>
<a href="#Squirtle">Squirtle.py</a> A simple pixel animation in terminal.<br>


## <div id="Imresize">Imresize.py</div>
## <div id="Kivy">Kivy_animation_1.py</div>

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

An example:<br>
```
Imresize.py -iReflection_of_the_Kanas_Lake_by_Wang_Jinyu.jpgFailed -w 300
```

<p align='center' >
<img src='img/Re_Imresize.png'>
</p>

## <div id="Kivy">Kivy_animation_1.py</div>

This script is orign from tshirtman, https://gist.github.com/tshirtman/5466755.<br>
I customized it to python3.<br>
If there has any offensive, please contack me and I will deleted it.

```
python3.7 Kivy_animation_1.py
```

<p align='center' >
<img src='img/Kivy_anim.gif'>
</p>

## <div id="Squirtle">Squirtle.py</div>

This is a simple pixel Squirtle animation in terminal.

```
python3.7 Squirtle.py
```
<p align='center' >
<img src='img/Squirtle.gif'>
</p>

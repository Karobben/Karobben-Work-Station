

# Karobben-Work-Station

[DontouchWhite.py](#Dontouch): A script for playing a web game  
[GPS_get.py](#GPS): There are two scripts working in different regions
[Imresize.py](#Imresize) A light image/imges resize python script for resizing one or a group of img.
[Kivy_animation_1.py](#Kivy): A example of animation in Kivy.
[Squirtle.py](#Squirtle): A simple pixel animation in terminal.
[pikachusay.py](#pikachusay): A simple pixel animation in terminal.
[txt2pdf](#txt2pdf): A script to convert text file to pdf file.
[Video_speed.py](#Video_speed): A script to speed up your video by dropping or increasing the frames
[abi_plot.py](#abi_plot): A script to speed up your video by dropping or increasing the frames




## <div id="Dontouch">DontouchWhite.py</div>

This script is using PIL to read the img from the screen and using OpenCV to read and find the target bin, and using pynput to click the target.

for more, please go to see:

https://www.bilibili.com/video/av86328254

## <div id="GPS">GPS_get.py</div>

GPS-get_geojs.py is using crawling based on requests. It works fine if you can easily achieve https://get.geojs.io. So, it is not friendly for some regions.<br>
The time consuming process is acquiring your IP address. So, you can speed it up by providing IP address yourself.

GPS-get_geocoder.py is using geocoder lib and it is super elegant. You can print your region and GPS coordinate with only three lines of code.

And for my personal experience, the result of geocoder is a little better than the result of geojs.

Both scripts should work:


```bash
python3 GPS-get_geojs.py
python3 GPS-get_geocoder.py
```

And you can pin the GPS coordinate on maps in http://www.gpsspg.com/maps.htm




## <div id="Imresize">Imresize.py</div>


### Single Img
```bash
Imresize.py -i input.png  #w=w/2, h=h/2
Imresize.py -i input.png -w #900 #w=900
Imresize.py -i input.png -t #900 #h=900
Imresize.py -i input.png -r 4 #w=w/4, h=h/4
```
You can resize img/imgs by width(-w), by height(-t), by both(-w -t) or by ratio(-r).<br>
You can also read one img each time, with default arguments, output file names as "Re_" + input.png.<br>

### Multiple Images
You can resize a group of img by using: -i *.png (the quotation marks here can not be omitted). The result will be importted to a directory with the same name.<br>
You can also read all imgs form a directory(single directory each). The way output is the same as when you read a bunch of img in a time.

An example:  

```bash
Imresize.py -i 1.png 2.png -w 300
Imresize.py -i *.png  -w 300
Imresize.py -i img/ -w 300
```

### Customizing Output formate

`Imresize.py -i *.png -w 300 -o Re_size -f jpg`
![alhmfU.jpg](https://s1.ax1x.com/2020/07/31/alhmfU.jpg)


## Update:

2020/2/9: Add print information function

```bash
Imresize.py -i "*" -inf 1
```
![alhZkV.jpg](https://s1.ax1x.com/2020/07/31/alhZkV.jpg)


2020/2/16  
1. Reading files as a list
2. Printing inf without extra arguments.  
3. Formatting all Output files

Printing img(s) inf

`Imresize.py -i * -inf`

Formatting Output images

Output all imgs as jpg formate
`Imresize2.py -i *.png -f  jpg`


## <div id="Kivy">Kivy_animation_1.py</div>

This script is origin from tshirtman, https://gist.github.com/tshirtman/5466755.<br>
I customized it to python3.<br>
If there has any offensive, please contack me and I will deleted it.

```
python3.7 Kivy_animation_1.py
```

![Kivy_animation.gif](https://s1.ax1x.com/2020/07/31/alhKl4.gif)

## <div id="Squirtle">Squirtle.py</div>

This is a simple pixel Squirtle animation in terminal.

```bash
python3.7 Squirtle.py
```
[![Squirtle.gif](https://s1.ax1x.com/2020/07/31/alheYT.gif)](https://imgchr.com/i/alheYT)


## <div id="pikachusay">pikachusay.py</div>

```bash
python pikachusay.py "hello world"
```
![alhupF.gif](https://s1.ax1x.com/2020/07/31/alhupF.gif)

## <div id="txt2pdf">txt2pdf</div>
from: [baruchel](https://github.com/baruchel/txt2pdf)

**Quick start**:
```bash
txt2pdf -s 12 -o document.pdf document.txt

# -s font size
# -o output
```

## <div id="Video_speed">Video_speed.py</div>
A script to speed up your video by dropping or increasing the frames

```python
Video_speed.py -i input.mpf -o outpu.mp4 -r 20

# -i input video
# -o output video
# -r dropping frames by ratio
# -f fps, default: the same as the origin one
# -inf show current fps  
```

## <div id="abi_plot">abi_plot.py</div>
This script is for visulazing the abi sequencing file.
At present, it can only plot the raw signal from the origin result.
```bash
abi_plot.py -i abi_file -o result.png
```
[![wmCyRJ.md.png](https://s1.ax1x.com/2020/09/06/wmCyRJ.md.png)](https://imgchr.com/i/wmCyRJ)

96 ab1 results are stored at `abi_file`:
```bash
ls abi_file
```
<pre>
A01.78-1.CMV-F.YP12097991.A01.S7341.ab1             B09.26-1.VR1012-F.YP12098399.B09.S7341.ab1   D05.168-3.ZmU6-F2.YP12093773.D05.s7341.ab1             F01.NAC56-1300-2.GHeGFP-R.YP12097743.F01.s7341.ab1          G09.1300-CLUC-W33-6.GHMAI-CLUC-R.YP12097553.G09.S7341.ab1
A02.78-2.CMV-F.YP12097992.A02.S7341.ab1             B10.26-2.VR1012-F.YP12098400.B10.S7341.ab1   D06.168-4.ZmU6-F2.YP12093774.D06.s7341.ab1             F02.NAC56-1300-2.GHpSuperF.YP12097744.F02.s7341.ab1         G10.1300-CLUC-W33-7.GHMAI-CLUC-F.YP12097554.G10.S7341.ab1
A03.78-3.CMV-F.YP12097993.A03.S7341.ab1             B11.15-1.VR1012-F.YP12098401.B11.S7341.ab1   D07.168-5.ZmU6-F2.YP12093775.D07.s7341.ab1             F03.NAC56-1300-3.GHeGFP-R.YP12097745.F03.s7341.ab1          G11.1300-CLUC-W33-7.GHMAI-CLUC-R.YP12097555.G11.S7341.ab1
'A04.CM4.(Y6249)indpro-F.YP12094362.A04.S7341.ab1'   B12.15-2.VR1012-F.YP12098402.B12.S7341.ab1   D08.FS7.M13F.YP12098873.D08.s7341.ab1                  F04.NAC56-1300-3.GHpSuperF.YP12097746.F04.s7341.ab1         G12.1300-CLUC-W33-9.GHMAI-CLUC-F.YP12097558.G12.S7341.ab1
A05.CB-3.EGFP-R.YP12094364.A05.S7341.ab1            C01.1-1.6F.YP12097892.C01.S7341.ab1          D09.OMS-1.PABAL-F.YP12097115.D09.s7341.ab1             F05.NAC56-1300-4.GHeGFP-R.YP12097747.F05.s7341.ab1          H01.1300-CLUC-W33-9.GHMAI-CLUC-R.YP12097559.H01.S7341.ab1
A06.C1F-A-4.EGFP-R.YP12094366.A06.S7341.ab1         C02.1-1.6R.YP12097893.C02.S7341.ab1          D10.OMS-1.PABAL-R.YP12097116.D10.s7341.ab1             F06.NAC56-1300-4.GHpSuperF.YP12097748.F06.s7341.ab1         H02.1300-CLUC-W33-10.GHMAI-CLUC-F.YP12097560.H02.S7341.ab1
A07.CA-4.EGFP-R.YP12094365.A07.S7341.ab1            C03.1-2.6F.YP12097894.C03.S7341.ab1          D11.OMS-2.PABAL-F.YP12097117.D11.s7341.ab1             F07.NAC56-1300-5.GHeGFP-R.YP12097749.F07.s7341.ab1          H03.1300-CLUC-W33-10.GHMAI-CLUC-R.YP12097561.H03.S7341.ab1
A08.EW-1.NOS.YP12097661.A08.S7341.ab1               C04.1-2.6R.YP12097895.C04.S7341.ab1          D12.OMS-2.PABAL-R.YP12097118.D12.s7341.ab1             F08.NAC56-1300-5.GHpSuperF.YP12097750.F08.s7341.ab1         H04.1300-CLUC-W33-11.GHMAI-CLUC-F.YP12097562.H04.S7341.ab1
A09.EW-2.NOS.YP12097662.A09.S7341.ab1               C05.1-3.6F.YP12097896.C05.S7341.ab1          E01.OMS-3.PABAL-F.YP12097119.E01.s7341.ab1             F09.NAC56-1302.GHCDN-1302-W1-R.YP12097751.F09.S7341.ab1     H05.1300-CLUC-W33-11.GHMAI-CLUC-R.YP12097563.H05.S7341.ab1
A10.EW-4.NOS.YP12097663.A10.S7341.ab1               C06.1-3.6R.YP12097897.C06.S7341.ab1          E02.OMS-3.PABAL-R.YP12097120.E02.s7341.ab1             F10.1300-CLUC-W33-1.GHMAI-CLUC-F.YP12097542.F10.S7341.ab1   H06.1300-CLUC-W33-12.GHMAI-CLUC-F.YP12097564.H06.S7341.ab1
A11.EZ-3.NOS.YP12097664.A11.S7341.ab1               C07.1-4.6F.YP12097898.C07.S7341.ab1          E03.1-1.GV1300-F.YP12094027.E03.S7341.ab1              F11.1300-CLUC-W33-1.GHMAI-CLUC-R.YP12097543.F11.S7341.ab1   H07.1300-CLUC-W33-12.GHMAI-CLUC-R.YP12097565.H07.S7341.ab1
A12.EZ-4.NOS.YP12097665.A12.S7341.ab1               C08.1-4.6R.YP12097899.C08.S7341.ab1          E04.1-1.GV1300-R.YP12094028.E04.S7341.ab1              F12.1300-CLUC-W33-2.GHMAI-CLUC-F.YP12097544.F12.S7341.ab1   H08.1300-CLUC-W33-13.GHMAI-CLUC-F.YP12097566.H08.S7341.ab1
B01.DN50SDD-2.M13F.YP12097666.B01.S7341.ab1         C09.167-1.ZmU6-F2.YP12093757.C09.s7341.ab1   E05.1-2.GV1300-F.YP12094029.E05.S7341.ab1              G01.1300-CLUC-W33-2.GHMAI-CLUC-R.YP12097545.G01.S7341.ab1   H09.1300-CLUC-W33-13.GHMAI-CLUC-R.YP12097567.H09.S7341.ab1
B02.DN50SDD-1.M13F.YP12097667.B02.S7341.ab1         C10.168-1.ZmU6-F2.YP12093758.C10.s7341.ab1   E06.1-2.GV1300-R.YP12094030.E06.S7341.ab1              G02.1300-CLUC-W33-3.GHMAI-CLUC-F.YP12097546.G02.S7341.ab1   H10.1300-CLUC-W33-8.GHMAI-CLUC-F.YP12097556.H10.S7341.ab1
B03.DN50SDD-3.M13F.YP12097668.B03.S7341.ab1         C11.167-2.ZmU6-F2.YP12093767.C11.s7341.ab1   E07.AP2-NLUC-1.GHmaiNlucR.YP12097735.E07.S7341.ab1     G03.1300-CLUC-W33-3.GHMAI-CLUC-R.YP12097547.G03.S7341.ab1   H11.1300-CLUC-W33-8.GHMAI-CLUC-R.YP12097557.H11.S7341.ab1
B04.SN10-3-SOD.M13F.YP12097669.B04.S7341.ab1        C12.167-3.ZmU6-F2.YP12093768.C12.s7341.ab1   E08.AP2-NLUC-3.GHmaiNlucR.YP12097737.E08.S7341.ab1     G04.1300-CLUC-W33-4.GHMAI-CLUC-F.YP12097548.G04.S7341.ab1   H12.Y-Y-Y.ab1
B05.1.M13F.YP12098395.B05.S7341.ab1                 D01.167-4.ZmU6-F2.YP12093769.D01.s7341.ab1   E09.AP2-NLUC-4.GHmaiNlucR.YP12097738.E09.S7341.ab1     G05.1300-CLUC-W33-4.GHMAI-CLUC-R.YP12097549.G05.S7341.ab1
B06.4.M13F.YP12098396.B06.S7341.ab1                 D02.167-5.ZmU6-F2.YP12093770.D02.s7341.ab1   E10.AP2-NLUC-5.GHmaiNlucR.YP12097739.E10.S7341.ab1     G06.1300-CLUC-W33-5.GHMAI-CLUC-F.YP12097550.G06.S7341.ab1
B07.7.M13F.YP12098397.B07.S7341.ab1                 D03.167-6.ZmU6-F2.YP12093771.D03.s7341.ab1   E11.AP2-NLUC-6.GHmaiNlucR.YP12097740.E11.S7341.ab1     G07.1300-CLUC-W33-5.GHMAI-CLUC-R.YP12097551.G07.S7341.ab1
B08.10.M13F.YP12098398.B08.S7341.ab1                D04.168-2.ZmU6-F2.YP12093772.D04.s7341.ab1   E12.NAC56-1300-1.GHmaiNlucR.YP12097741.E12.S7341.ab1   G08.1300-CLUC-W33-6.GHMAI-CLUC-F.YP12097552.G08.S7341.ab1
</pre>

# abi_plot.py
This script is for plotting ab1 result. So, You need a directory with ab1 files.

# Statistic.R
This is my personal script. Just ignore it, please. I'll delete it later

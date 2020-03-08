# WuxiaWorld PDF Converter

### Instalation
```bash
#clone repo
$ git clone https://github.com/gutessitore/WuxiaWorldPDFConverter.git

#change to working directory
$ cd WuxiaWorldPDFConverter

#install requirements
$ python3 setup.py
```
### Usage
```bash
Usage: WuxiaWorldPDFConverter.py [-h] [-a] [-l <link>] [-s <number>] [-e <number>]
Arguments: 
 -h, --help     Show this help message and exit
 --all, -a       Convert all chapters (may have teasers from last chapters)
 -l <link>       Link from any chapter of the novel
 -s <number>     Number of the first desired chapter
 -e <number>     Number of the last desired chapter

```
To convert specific chapters
```bash
$python3 -l  https://www.wuxiaworld.com/novel/emperors-domination/emperor-chapter-12 -s 5 -e 10
```
To convert all chapters
```bash
$python3 --all -l  https://www.wuxiaworld.com/novel/emperors-domination/emperor-chapter-12
```
The output file will be a pdf named `<novel-name>_Chapters_<start>-<end>.pdf`
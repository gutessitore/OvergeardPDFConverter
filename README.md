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
To convert specific chapters
```bash
$python3 -l  https://www.wuxiaworld.com/novel/emperors-domination/emperor-chapter-12 -s 5 -e 10
```
To convert all chapters
```bash
$python3 --all -l  https://www.wuxiaworld.com/novel/emperors-domination/emperor-chapter-12
```
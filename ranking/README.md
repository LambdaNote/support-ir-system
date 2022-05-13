1. Docker imageの作成

```
$ docker build -t lightgbm-ranking .
```

2. MSLR-WEB10Kデータセットをsvmlight形式からcsv形式に変換する

trainデータの変換
```
$ docker run --rm -v <MSLR-WEB10K dataset path>/train.txt:/train.txt -v /tmp:/tmp lightgbm-ranking python svmlight2csv.py /train.txt -o /tmp/train.csv
```

validationデータの変換
```
$ docker run --rm -v <MSLR-WEB10K dataset path>/vali.txt:/vali.txt -v /tmp:/tmp lightgbm-ranking python svmlight2csv.py /vali.txt -o /tmp/valid.csv
```

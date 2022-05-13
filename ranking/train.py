import argparse
import lightgbm as lgb


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("train_csv")
    parser.add_argument("valid_csv")
    args = parser.parse_args()

    # 学習データの読み込み設定
    load_params = {
        # csvファイルにヘッダが存在するときに指定
        "header": "true",
        # "qid"列をクエリID列とする
        "group_column": "name:qid"
    }

    train_data = lgb.Dataset(args.train_csv, params=load_params)
    valid_data = lgb.Dataset(args.valid_csv, params=load_params)

    # 学習設定
    train_params = {
        # LambdaMARTによるランキング学習
        "objective": "lambdarank",
        # NDCGで精度評価する
        "metric": "ndcg",
        # NDCG@kのkを指定する
        "ndcg_eval_at": "1,3"
    }

    # 学習実行
    model = lgb.train(train_params, train_data, valid_sets=[valid_data])

from django.shortcuts import render

def detail_place (request,pk):
    #GET　place placecommentを取得する
    #POSTの中でplacecommentが保存できる　神社の詳細画面でコメントが追加できる
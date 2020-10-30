from os import walk
from google.cloud import translate_v2 as translate
import re
import json

auth = open("./creds.json")
jsonAuth = json.load(auth)
auth.close()
print(jsonAuth)


translate_client = translate.Client()
for (repertoire, sousRepertoires, fichiers) in walk("./vocab/"):
  for file in fichiers:
    # result = re.match(r'(.*)_k.txt',file)
    # if result:
    #   f = open(repertoire+'/'+file)
    #   r = open(repertoire+'/'+result.group(1)+'_k.quizlet',"w")
    #   for char in f.read():
    #     trad = translate_client.translate(char, target_language='fr',source_language='ja')
    #     r.write(char+','+trad["translatedText"]+'\n')
    #   r.close()
    #   f.close()
    result = re.match(r'(.*)_v.txt',file)
    if result:
      f = open(repertoire+'/'+file)
      r = open(repertoire+'/'+result.group(1)+'_v.quizlet',"w")
      for line in f.readlines():
       reg = re.match(r'.*;(.*)',line)
       vocab=reg.group(1)
       trad = translate_client.translate(vocab, target_language='fr',source_language='ja')
       r.write(vocab+','+trad["translatedText"]+'\n')
      f.close()
      r.close()

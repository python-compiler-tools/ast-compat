rbnf-pygen.exe ./asdl.exrbnf ./asdl.rlex ./asdl_parse.tmp.py --k 1 --traceback
echo "from parser_rts import *" > ./asdl_parse.py
cat ./asdl_parse.tmp.py >> ./asdl_parse.py
rm ./asdl_parse.tmp.py
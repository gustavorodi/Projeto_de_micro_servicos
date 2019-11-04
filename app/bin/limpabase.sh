#! /bin/bash
source bin/helper.sh

for i in *.db ; do
    rm $i
done
python tabela.py
success "Finalizado com suscesso!"

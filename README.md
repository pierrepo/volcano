# Projet volcano : outils de visualisation et d'analyse de données en protéomique quantitative


## Dépôts

- [Dépôt](https://github.com/pierrepo/volcano-f) (privé) de [Fabien](https://github.com/fab-genty)
- [Dépôt](https://github.com/pierrepo/volcano-n) (privé) de [Nicolas](https://github.com/NicolasBRUNEAU)

La licence *BSD 3-clause* est très bien. On peut la trouver [ici](https://github.com/Candihub/pixel/blob/master/LICENSE).

Organisation du dépôt :

    volcano/             répertoire contenant les fichiers du serveur web
    README.md           notice d'installation et d'utilisation
    requirements.txt    paquets Python à installer avec pip

Un exemple de [README.md](https://github.com/pierrepo/cours-python/blob/master/README.md)

## Ressources web

### Frameworks CSS

- Zurb [Foundation](https://foundation.zurb.com/) : doc d'[installation](https://foundation.zurb.com/sites/docs/)
- Twitter [Bootstrap](http://getbootstrap.com/) : doc d'[installation](https://foundation.zurb.com/sites/docs/)


### Tableau dynamique

Tri des colonnes et moteur de recherche

- [DataTables](https://datatables.net/examples/basic_init/multi_col_sort.html)
- [Dynatable.js](https://www.dynatable.com/)

Il en existe d'autres.


## Accès aux données et conversion


### API web du NCBI 

Pour la conversion d'un numéro d'accession vers un autre

- [Entrez Programming Utilities Help](https://www.ncbi.nlm.nih.gov/books/NBK25501/)
- [Converting GI numbers to accession numbers](https://www.ncbi.nlm.nih.gov/books/NBK25498/#chapter3.Application_1_Converting_GI_num)


### API web d'UniProt

La conversion d'un numéro d'accession vers un autre peut se faire en ligne sur le site d'UniProt, via l'outil [Retrieve/ID mapping](http://www.uniprot.org/uploadlists/). Il faut copier/coller des identifiants dans la zone *Provide your identifiers* puis sélectionner les options *From* (par exemple *GI number*) et *To* (par exemple *UniProtKB*, pour obtenir les identifiants UniProt).

Cette fonctionnalité est également disponible sous la forme d'une [API](http://www.uniprot.org/help/api). Quelques exemples de l'utilisation de l'API sont disponibles dans le script Python 3 `uniprot_map_identifiers.py`.

Attention, un même identifiant *GI* peut conduire à deux protéines dans UniProt, en général avec le status *reviewed* et *unreviewed*. Si c'est le cas, ne prendre que la protéine *reviewed*.

Par ailleurs, les informations d'une protéine sont directement accessibles via une URL. Par exemple, pour la protéine *P12345* :

- La fiche de la protéine : <http://www.uniprot.org/uniprot/P12345>
- La même chose au format TXT <http://www.uniprot.org/uniprot/P12345.txt>
- La même chose au foramt XML <http://www.uniprot.org/uniprot/P12345.xml>

Voir la documentation [Retrieving individual entries](http://www.uniprot.org/help/api_retrieve_entries) pour plus d'exemples.

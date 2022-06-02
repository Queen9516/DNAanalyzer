from Bio.Blast import NCBIWWW

## Enter NCBI accession number as the 3rd argument below.
result_handle = NCBIWWW.qblast("blastn", "nt", "MT263381", hitlist_size=200,  format_type='XML')
f=open("xml_files/blast3.xml","w+")
f.write(result_handle.read())
f.close()

{\rtf1\ansi\ansicpg1252\cocoartf1671\cocoasubrtf200
{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\paperw11900\paperh16840\margl1440\margr1440\vieww10800\viewh8400\viewkind0
\pard\tx566\tx1133\tx1700\tx2267\tx2834\tx3401\tx3968\tx4535\tx5102\tx5669\tx6236\tx6803\pardirnatural\partightenfactor0

\f0\fs24 \cf0 Number of inactive ads :\
\
\pard\tx566\tx1133\tx1700\tx2267\tx2834\tx3401\tx3968\tx4535\tx5102\tx5669\tx6236\tx6803\pardirnatural\partightenfactor0
\cf0 \'ab\'a0SELECT count(S.id)\
FROM Stuff S \
WHERE owner = %s\'a0AND NOT EXIST(SELECT 1 FROM Stuff S join LoanProposition LP ON S.id = LP.id)\'bb,  [o.user_id] \
\pard\tx566\tx1133\tx1700\tx2267\tx2834\tx3401\tx3968\tx4535\tx5102\tx5669\tx6236\tx6803\pardirnatural\partightenfactor0
\cf0 \
Number of active ads :\
\
\'ab\'a0SELECT count(id)\
FROM LoanProposition\
WHERE owner = %s\'a0\'bb,  [o.user_id]\
\
Most used Tags :\
\
query = \'ab\'a0SELECT tags FROM Stuff WHERE owner=%s\'a0\'bb, [o.user_id]\
repeated_tags=[]\
distinct_tags=[]\
for ligne in query:\
	tab=ligne.split(\'ab\'a0,\'a0\'bb)\
	for word in tab:\
		if word.lower() not in distinct_tags:\
			distinct_tags.append(word.lower())\
	repeated_tags+=tab\
	max=0\
	most_used_tags=[]\
	for tag in distinct_tags:\
		nb=repeated_tags.count(tag)\
		if nb > max :\
			max = nb\
			most_used_tags=[tag]\
		if nb = max :\
			most_used_tags.append[tag]\
\'97> il faut afficher most_used_tags\
\
\
Average duration of your ads:\
\
\'ab\'a0SELECT AVG(end_date - start_date) \
FROM LoanProposition\
WHERE owner=%s\'a0\'bb , [o.user_id]\
\
nb of request:\
\
\'ab\'a0SELECT count(LR.loan_id)\
FROM LoanRequest LR Join LoanProposition LP on LR.original_Proposition = LP.id\
WHERE LP.owner=%s\'a0\'bb, [o.user_id]\
\
\
}
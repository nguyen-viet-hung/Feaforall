import os,sys

commFilePath = os.path.join('/home/cyprien/Desktop/yacs-example', "RunCase_1_Stage_1.comm")

commString="""DEBUT(LANG='EN')


mesh = LIRE_MAILLAGE(identifier=u'0:1',
                     UNITE=20)

model = AFFE_MODELE(identifier=u'1:1',
                    AFFE=_F(MODELISATION=('3D', ),
                            PHENOMENE='MECANIQUE',
                            TOUT='OUI'),
                    MAILLAGE=mesh)

mater = DEFI_MATERIAU(identifier=u'2:1',
                      ELAS=_F(E="""+str(E)+""",
                              NU="""+str(NU)+"""))

fieldmat = AFFE_MATERIAU(identifier=u'3:1',
                         AFFE=_F(MATER=(mater, ),
                                 TOUT='OUI'),
                         MODELE=model)

load = AFFE_CHAR_MECA(identifier=u'4:1',
                      DDL_IMPO=_F(GROUP_MA=('xmin', ),
                                  LIAISON='ENCASTRE'),
                      MODELE=model,
                      PRES_REP=_F(GROUP_MA=('xmax', ),
                                  PRES=-200.0))

reslin = MECA_STATIQUE(identifier=u'5:1',
                       CHAM_MATER=fieldmat,
                       EXCIT=_F(CHARGE=load),
                       MODELE=model)

reslin = CALC_CHAMP(identifier=u'6:1',
                    reuse=reslin,
                    CRITERES=('SIEQ_ELGA', 'SIEQ_ELNO', 'SIEQ_NOEU'),
                    RESULTAT=reslin)

IMPR_RESU(identifier=u'7:1',
          FORMAT='MED',
          RESU=_F(RESULTAT=reslin),
          UNITE=80)

IMPR_RESU(identifier=u'8:1',
          FORMAT='RESULTAT',
          RESU=_F(NOM_CHAM=('DEPL', ),
                  RESULTAT=reslin,
                  VALE_MAX='OUI',
                  VALE_MIN='OUI'),
          UNITE=2)

FIN()"""


commFile = open(commFilePath,'w')
commFile.write(commString)
commFile.close()

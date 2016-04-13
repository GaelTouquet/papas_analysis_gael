import heppy.framework.config as cfg
from xrootd import xrootd

single_charged_hadrons_lfns = [
    '/store/mc/RunIISpring15DR74/SinglePiPlus_P-1to2000_Expo_13TeV_ExpoRandomPGun/GEN-SIM-RECO/AsymptNoPUReco_MCRUN2_74_V9A-v1/00000/02176367-450E-E511-81F4-003048FF9AC6.root',
    '/store/mc/RunIISpring15DR74/SinglePiPlus_P-1to2000_Expo_13TeV_ExpoRandomPGun/GEN-SIM-RECO/AsymptNoPUReco_MCRUN2_74_V9A-v1/00000/107E5C6C-450E-E511-A97E-0025905B85D8.root',
    '/store/mc/RunIISpring15DR74/SinglePiPlus_P-1to2000_Expo_13TeV_ExpoRandomPGun/GEN-SIM-RECO/AsymptNoPUReco_MCRUN2_74_V9A-v1/00000/127017F4-450E-E511-8AA7-0025905B85D6.root',
    '/store/mc/RunIISpring15DR74/SinglePiPlus_P-1to2000_Expo_13TeV_ExpoRandomPGun/GEN-SIM-RECO/AsymptNoPUReco_MCRUN2_74_V9A-v1/00000/18B37F1A-460E-E511-9633-003048FFD732.root',
    '/store/mc/RunIISpring15DR74/SinglePiPlus_P-1to2000_Expo_13TeV_ExpoRandomPGun/GEN-SIM-RECO/AsymptNoPUReco_MCRUN2_74_V9A-v1/00000/1E6CDDFD-450E-E511-9965-00259059642E.root',
    '/store/mc/RunIISpring15DR74/SinglePiPlus_P-1to2000_Expo_13TeV_ExpoRandomPGun/GEN-SIM-RECO/AsymptNoPUReco_MCRUN2_74_V9A-v1/00000/2CA26267-450E-E511-A377-003048FF9AC6.root',
    '/store/mc/RunIISpring15DR74/SinglePiPlus_P-1to2000_Expo_13TeV_ExpoRandomPGun/GEN-SIM-RECO/AsymptNoPUReco_MCRUN2_74_V9A-v1/00000/3CB62A9D-9B0E-E511-9F74-002354EF3BDB.root',
    '/store/mc/RunIISpring15DR74/SinglePiPlus_P-1to2000_Expo_13TeV_ExpoRandomPGun/GEN-SIM-RECO/AsymptNoPUReco_MCRUN2_74_V9A-v1/00000/465098F7-430E-E511-9332-0025905A60A6.root',
    '/store/mc/RunIISpring15DR74/SinglePiPlus_P-1to2000_Expo_13TeV_ExpoRandomPGun/GEN-SIM-RECO/AsymptNoPUReco_MCRUN2_74_V9A-v1/00000/4C0EBD12-450E-E511-9871-0025905B858A.root',
    '/store/mc/RunIISpring15DR74/SinglePiPlus_P-1to2000_Expo_13TeV_ExpoRandomPGun/GEN-SIM-RECO/AsymptNoPUReco_MCRUN2_74_V9A-v1/00000/5418D162-470E-E511-B171-00261894397D.root',
    '/store/mc/RunIISpring15DR74/SinglePiPlus_P-1to2000_Expo_13TeV_ExpoRandomPGun/GEN-SIM-RECO/AsymptNoPUReco_MCRUN2_74_V9A-v1/00000/6645CACD-440E-E511-B43F-0002C90A36FE.root',
    '/store/mc/RunIISpring15DR74/SinglePiPlus_P-1to2000_Expo_13TeV_ExpoRandomPGun/GEN-SIM-RECO/AsymptNoPUReco_MCRUN2_74_V9A-v1/00000/80DE1D68-490E-E511-AB6A-003048FFD7BE.root',
    '/store/mc/RunIISpring15DR74/SinglePiPlus_P-1to2000_Expo_13TeV_ExpoRandomPGun/GEN-SIM-RECO/AsymptNoPUReco_MCRUN2_74_V9A-v1/00000/82E2C4BE-450E-E511-8BF3-003048FFCB8C.root',
    '/store/mc/RunIISpring15DR74/SinglePiPlus_P-1to2000_Expo_13TeV_ExpoRandomPGun/GEN-SIM-RECO/AsymptNoPUReco_MCRUN2_74_V9A-v1/00000/8C1AE911-460E-E511-BA37-002618943885.root',
    '/store/mc/RunIISpring15DR74/SinglePiPlus_P-1to2000_Expo_13TeV_ExpoRandomPGun/GEN-SIM-RECO/AsymptNoPUReco_MCRUN2_74_V9A-v1/00000/8CF8C273-450E-E511-A0F8-003048FFD7C2.root',
    '/store/mc/RunIISpring15DR74/SinglePiPlus_P-1to2000_Expo_13TeV_ExpoRandomPGun/GEN-SIM-RECO/AsymptNoPUReco_MCRUN2_74_V9A-v1/00000/90EDD4A9-450E-E511-8E95-A0040420FE80.root',
    '/store/mc/RunIISpring15DR74/SinglePiPlus_P-1to2000_Expo_13TeV_ExpoRandomPGun/GEN-SIM-RECO/AsymptNoPUReco_MCRUN2_74_V9A-v1/00000/9608E7C7-440E-E511-BE19-0025905A6138.root',
    '/store/mc/RunIISpring15DR74/SinglePiPlus_P-1to2000_Expo_13TeV_ExpoRandomPGun/GEN-SIM-RECO/AsymptNoPUReco_MCRUN2_74_V9A-v1/00000/ACC7244D-430E-E511-9A7B-A0369F3016EC.root',
    '/store/mc/RunIISpring15DR74/SinglePiPlus_P-1to2000_Expo_13TeV_ExpoRandomPGun/GEN-SIM-RECO/AsymptNoPUReco_MCRUN2_74_V9A-v1/00000/B6F502AD-450E-E511-91F4-0002C90B740E.root',
    '/store/mc/RunIISpring15DR74/SinglePiPlus_P-1to2000_Expo_13TeV_ExpoRandomPGun/GEN-SIM-RECO/AsymptNoPUReco_MCRUN2_74_V9A-v1/00000/C2BFC073-450E-E511-BAD5-003048FFD7C2.root',
    '/store/mc/RunIISpring15DR74/SinglePiPlus_P-1to2000_Expo_13TeV_ExpoRandomPGun/GEN-SIM-RECO/AsymptNoPUReco_MCRUN2_74_V9A-v1/00000/DE9B9D6F-470E-E511-A4FA-0002C92DB464.root',
    '/store/mc/RunIISpring15DR74/SinglePiPlus_P-1to2000_Expo_13TeV_ExpoRandomPGun/GEN-SIM-RECO/AsymptNoPUReco_MCRUN2_74_V9A-v1/00000/E6616906-440E-E511-B747-0025905A48D8.root',
    '/store/mc/RunIISpring15DR74/SinglePiPlus_P-1to2000_Expo_13TeV_ExpoRandomPGun/GEN-SIM-RECO/AsymptNoPUReco_MCRUN2_74_V9A-v1/00000/EA587EAB-430E-E511-8EDB-00259059649C.root',
    '/store/mc/RunIISpring15DR74/SinglePiPlus_P-1to2000_Expo_13TeV_ExpoRandomPGun/GEN-SIM-RECO/AsymptNoPUReco_MCRUN2_74_V9A-v1/00000/F29D5B8D-9B0E-E511-805B-B8CA3A709648.root',
    ]

single_charged_hadrons = cfg.Component(
    'single_charged_hadrons',
    # files = ['/gridgroup/cms/cbernet/data/singlePi_50k.root']
    files = map(xrootd, single_charged_hadrons_lfns)
    )

single_neutral_hadrons = cfg.Component(
    'single_neutral_hadrons',
    files = ['/gridgroup/cms/cbernet/data/singleK0L.root']
    )

single_photons = cfg.Component(
    'single_photons',
    files = ['/gridgroup/cms/cbernet/data/singlePhoton.root']
    )

if __name__ == '__main__':
    print single_charged_hadrons

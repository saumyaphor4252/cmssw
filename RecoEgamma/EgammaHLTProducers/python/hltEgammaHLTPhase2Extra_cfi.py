import FWCore.ParameterSet.Config as cms

hltEgammaHLTPhase2Extra = cms.EDProducer(
    "EgammaHLTPhase2ExtraProducer",

    # Input from the first producer
    egTrigObjs = cms.InputTag("hltEgammaHLTExtra"),

    # L1 + truth matching inputs
    l1Trks = cms.InputTag("l1tTTTracksFromTrackletEmulation", "Level1TTTracks"),
    trkParts = cms.InputTag("mix", "MergedTrackTruth"),
    l1TrkToTrkPartMap = cms.InputTag("TTTrackAssociatorFromPixelDigis", "Level1TTTracks"),

    # HGCal clusters + timing
    hgcalLayerClusters = cms.InputTag("hgcalLayerClusters"),
    hgcalLayerClustersTime = cms.InputTag("hgcalLayerClusters", "timeLayerCluster"),

    # HGCal RecHits (VPSet like your first module style)
    hgcal = cms.VPSet(
        cms.PSet(
            src = cms.InputTag("HGCalRecHit", "HGCEERecHits"),
            label = cms.string("HGCEERecHits")
        ),
        cms.PSet(
            src = cms.InputTag("HGCalRecHit", "HGCHEFRecHits"),
            label = cms.string("HGCHEFRecHits")
        ),
        cms.PSet(
            src = cms.InputTag("HGCalRecHit", "HGCHEBRecHits"),
            label = cms.string("HGCHEBRecHits")
        )
    ),

    # Same filtering knobs as first producer
    minPtToSaveHits = cms.double(0.0),
    saveHitsPlusPi = cms.bool(True),
    saveHitsPlusHalfPi = cms.bool(True),

    # Phase-2 specific: RecHit counting thresholds
    recHitCountThresholds = cms.vdouble(0.0, 0.5, 1.0, 1.5, 2.0)
)

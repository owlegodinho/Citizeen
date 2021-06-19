from sentinelhub import SHConfig, MimeType, CRS, BBox, DataCollection, WmsRequest, SentinelHubRequest, Geometry

ndviRequest = SentinelHubRequest(

    evalscript='''//VERSION=3

let viz = new HighlightCompressVisualizerSingle();

function evaluatePixel(samples) {
    let val = index(samples.B08, samples.B04);
    val = viz.process(val);
    val.push(samples.dataMask);
    return val;
}

function setup() {
  return {
    input: [{
      bands: [
        "B04",
        "B08",
        "dataMask"
      ]
    }],
    output: {
      bands: 2
    }
  }
}

''',
    
)
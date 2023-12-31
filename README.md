# Usage

1. Download the `nyu_depth_v2_labeled_data.pkl` directly, it contains all data in origin MATLAB version of Labeled Dataset. (I haven't upload it to this repo or to other network drives, it needs further clearing.)
2. Or you can follow the instruction below to generate it yourself (recommended now).

# Generation

1. Download the Labeled Dataset from official [website](https://cs.nyu.edu/~silberman/datasets/nyu_depth_v2.html). And place that `.mat` file at the same dir.
2. Using the `h5py` module to load the `.mat` file.
3. The `matrix` in `.mat` file can be correctly and easily read, don't bother it.
4. The `cell array` in `.mat` file should specially processed.
5. The `Map` in `.mat` file should also be treated specially, I got its keys and values in MATLAB and opened them in MATLAB as a table format (can be firstly transposed in MATLAB), then copy the keys and values table to Excel to concatenate as one table with two columns. Finally, saved the Excel file as CSV format.
6. Above is how to treat different types of data field in `.mat` file. I just put all that field in one dict, and saved them as a `pkl` file. (~5.8GB)

# Visualization

The images and depth images can be easily visualized by `matplotlib` module.

# TODO

- [ ] Maybe I will parse the something like the images out to a single directory, and just place string-like data in `.pkl` file.

# Citation

```bibtex
@inproceedings{Silberman:ECCV12,
  author    = {Nathan Silberman, Derek Hoiem, Pushmeet Kohli and Rob Fergus},
  title     = {Indoor Segmentation and Support Inference from RGBD Images},
  booktitle = {ECCV},
  year      = {2012}
}
```

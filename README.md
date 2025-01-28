# DaskRaha and DaskBaran

The semi-supervised approaches [Raha and Baran](https://github.com/BigDaMa/raha) display competitive performance in general cleaning scenarios. However the effectiveness comes at high runtime costs.
In this work, we improve the runtimes of Raha and Baran by proposing a new Dask-based parallel architecture that enhances CPU utilization. Further, we propose a shared memory model, allowing concurrently running workers to access shared objects, thereby reducing memory consumption by avoiding duplicated data for each worker. Our approach demonstrates significant runtime improvements compared to the previous versions of Raha and Baran, which are end-to-end holistic systems.


## Installation

Make sure you have Python 3.10 installed.

To install Raha and Baran with Dask using the github repository:
```console
git clone https://github.com/D2IP-TUB/DaskRahaBaran.git
cd DaskRahaBaran
pip install -e .[dask]
```

To uninstall them, you can run:
```console
pip uninstall daskrahabaran
```

## Usage
Running Raha and Baran is simple!
   - **Interactive data cleaning with Raha and Baran**: If you have a dirty dataset and you want to interatively detect and correct data errors, please check our interactive Jupyter notebook in the `raha` folder. The Jupyter notebook provides graphical user interfaces.
   ![Data Annotation](pictures/ui.png)   
   
Hint:
The pre-trained model inside the repo is only a sample for using the notebooks. Refrain from relying on that for your experiments. If you need to use the pre-trained models for Baran, please download the Wikipedia revision histories and use Baran to train a model.

## References
You can find more information about this project and the authors [here](https://vldb.org/workshops/2024/proceedings/QDB/QDB-1.pdf). You can also use the following bib entries to cite this project and the corresponding research papers.

### Citing DaskRahaRaha
```
@inproceedings{DBLP:conf/vldb/AhmadiMA24,
  author       = {Fatemeh Ahmadi and
                  Yusuf Mandirali and
                  Ziawasch Abedjan},
  title        = {Accelerating the Data Cleaning Systems Raha and Baran through Task
                  and Data Parallelism},
  booktitle    = {Proceedings of Workshops at the 50th International Conference on Very
                  Large Data Bases, {VLDB} 2024, Guangzhou, China, August 26-30, 2024},
  publisher    = {VLDB.org},
  year         = {2024},
  url          = {https://vldb.org/workshops/2024/proceedings/QDB/QDB-1.pdf},
  timestamp    = {Thu, 28 Nov 2024 13:37:37 +0100},
  biburl       = {https://dblp.org/rec/conf/vldb/AhmadiMA24.bib},
  bibsource    = {dblp computer science bibliography, https://dblp.org}
}
```

### Dask Version
The implementation for Raha and Baran with Dask was created by Yusuf Mandirali. The original code can be found [here](https://github.com/yimlyim/DaskRaha).

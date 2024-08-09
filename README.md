# jogramop-package

This repository is a packaged version of this one:
https://github.com/mrudorfer/jogramop-framework/

It contains the existing scenarios, without the scripts for creation of new ones.
The main advantage is that it can be conveniently installed using pip and then used in other projects.

For more details on jogramop, please visit our project website:
https://mrudorfer.github.io/jogramop-framework/

If you use this package for any research, please cite our publication:

M. Rudorfer, J. Hartvich, V. Vonasek: "A Framework for Joint Grasp and Motion Planning in Confined Spaces", 13th International Workshop on Robot Motion and Control (RoMoCo'24), 2024.

## Installation

```commandline
git clone git@github.com:mrudorfer/jogramop-package.git
cd jogramop-package
conda create -n jogramop python=3.10
conda activate jogramop
pip install git+https://github.com/mrudorfer/burg-toolkit@dev
pip install .
```

Potential issue:
If a cdktree/numpy bug comes up after `import burg_toolkit`, we were able to resolve it by reinstalling numpy and numba.

Please get in touch (create an issue) if you encounter any issues during installation.

## Visualizing scenarios

You can visualize a scenario using the following code:

```python
from jogramop.util import SCENARIO_IDS
from jogramop.scenario import Scenario
from jogramop.visualization import show_scenario

for i in SCENARIO_IDS:
    print(f'********** SCENARIO {i:03d} **********')
    s = Scenario(i)
    
    # select a random subset of grasps for better visualization
    s.select_n_grasps(10)
    
    show_scenario(s)
```

This repository comes with full robot simulation functionality based on pyBullet, see module `simulation.py`.
You can also use it directly to implement planners for these scenarios, see:
```python
from jogramop.scenario import Scenario

s = Scenario(11)
robot, sim = s.get_robot_and_sim(with_gui=True)
```

Finally, once we have a planning result, we can visualize it as well.
A plan is essentially a list of joint configurations which represent the waypoints when moving from start to goal.
```python
from jogramop.visualization import visualize_waypoints

visualize_waypoints(scenario, list_of_waypoints)
```


## Citation

If you use this work, please consider citing our publication:

M. Rudorfer, J. Hartvich and V. Vonásek, "[A Framework for Joint Grasp and Motion Planning in Confined Spaces](https://ieeexplore.ieee.org/document/10604306)," 2024 13th International Workshop on Robot Motion and Control (RoMoCo), Poznań, Poland, 2024, pp. 1-7, doi: 10.1109/RoMoCo60539.2024.10604306.

```
@INPROCEEDINGS{jogramop_2024,
  author={Rudorfer, Martin and Hartvich, Jiři and Vonásek, Vojtěch},
  booktitle={2024 13th International Workshop on Robot Motion and Control (RoMoCo)}, 
  title={A Framework for Joint Grasp and Motion Planning in Confined Spaces}, 
  year={2024},
  volume={},
  number={},
  pages={1-7},
  keywords={Robot motion;Annotations;Conferences;Grasping;Benchmark testing;Aerospace electronics;Planning},
  doi={10.1109/RoMoCo60539.2024.10604306}
}
```
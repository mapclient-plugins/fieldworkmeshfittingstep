Fieldwork Mesh Fitting Step
===========================
MAP Client plugin for fitting a Fieldwork mesh to a target pointcloud.

The coordinates of each node on the input mesh are optimised to minimise
the least-squared distance between the mesh surface and the target
points.

Theoretical details implemented in this plugin are described in

- Zhang, J., Malcolm, D., Hislop-Jambrich, J., Thomas, C.D.L., &
Nielsen, P.M.F. (2014). An Anatomical Region-based Statistical Shape
Model of the Human Femur. Computer Methods in Biomechanics and
Biomedical Engineering: Imaging & Visualization, 2(3), 176–185.
- Bradley, C.P., Pullan, A.J., & Hunter, P.J. (1997). Geometric
Modeling of the Human Torso Using Cubic. Annals of Biomedical
Engineering, 25, 96–111.

Requires
--------
- GIAS2 : https://bitbucket.org/jangle/gias2

Inputs
------
- **pointcloud** [nx3 NumPy Array] : The target point cloud.
- **fieldworkmodel** [GIAS2 GeometricField instance] : The Fieldwork
    mesh to be fitted.
- **array1d** [1-D NumPy Array] : An array of weights for each target
    point.

Outputs
-------
- **fieldworkmodel** [GIAS2 GeometricField instance] : The fitted slave
    mesh.
- **fieldworkmodelparameters** [NumPy Array] : An array of the fitted
    slave mesh parameters.
- **float** [float] : The registration error in terms of the
    root-mean-squared Euclidean distance between the target points and
    the fitted mesh.
- **array1d** [1-D NumPy Array] : An array of the Euclidean distance
    between each target point and its closest point on the fitted mesh.

Configuration
-------------
- **identifier** : Unique name for the step.
- **GUI** : [_True_|_False_] If the step GUI should be lauched on execution.
    Set to _False_ if running workflow in batch mode.
- **Fit Mode** : How distance is calculated in the fitting objective
    function.
	- _DPEP_ : Distance between each target point and its closest point on
        the input mesh. Points on the input mesh are sampled according
        to the "mesh discretisation" parameter.
	- _EPDP_ : Distance between each point on the input mesh and its
        closest target point. Points on the input mesh are sampled
        according to the "mesh discretisation" parameter.
- **mesh discretisation** : How densely the input mesh is to be sampled
    when calculating distance to or from the target points. High values 
    give a more accurate discretisation and a more accurate fit. Can be 
    one of two value formats:
    - if the format is _[d1,d2]_, _d1_ and _d2_ are the discretisation for
    each element in each element coordinate direction. E.g. _[5,5]_ means
    each 2-D quadralateral element will be discretised into 25 points. 
    The points are evenly distributed in the element coordinate system.
    - if the format is a single float _d_ (e.g. 5.0), each element is
    sub-divided until no points are more than distance _d_ apart in the 
    global coordinate system. This discretistion method produces more 
    evenly spaced points over the whole mesh. 
- **sobelov discretisation** : Slave mesh discretisation when
    calculating the Sobelov norm of the input mesh which penalises
    against regions of high curvature. Should of the format _[d1,d2]_ 
    where _d1_ and _d2_ are the discretisation for each element in each 
    element coordinate direction. Recommended values for different input 
    mesh orders:
	- 3 (cubic) : _[4,4]_
	- 4 (quartic) : _[5,5]_
- **sobelov weight** : Weights for each of the 5 terms of the input mesh
    Sobelov norm. Typical values: _[1e-5, 1e-5, 1e-5, 1e-5, 2e-5]_.
- **normal discretistaion** : Number of points to sample along an input 
    mesh element edge when calculating the element normal penalty term. 
    Recommended values for different slave mesh orders:
	- 3 (cubic) : _4_
	- 4 (quartic) : _5_
- **normal weight** : Weight on the input mesh element normal penalty
    term.
- **max iterations** : Max number of outer fitting iterations before 
    termination.
- **max sub-iterations** : Number of inner fitting iterations before 
    closest point distances are recalculated.
- **xtol** : Minimum relative error between successive objective 
    function evaluations before termination.
- **kdtree args** : optional arguments for the SciPy cKDTree.query 
    function when searching for closest target and input mesh points.
- **n closest points** : Number of closest points to find when 
    calculating distances between input mesh and target points.
- **verbose** : [_True_|_False_] print extra messages to commandline.
- **fixed nodes** : The numbers of nodes to be fixed in the fit.

Step GUI
--------
- **3D Scene** : Interactive viewer for the target point cloud, the 
    unfitted input mesh, and the fitted mesh.
- **Visibles box** : Show or hide objects in the 3D scene.
- **Fitting Parameters** : Parameters for the registration optimisation. 
    See the Configuration section for an explanation of the parameters.
- **Fit** : Run the fit using the given parameters.
- **Reset** : Removes the fitted input mesh.
- **Abort** : Abort the workflow.
- **Accept**: Finish the step and send outputs.
- **Fitting Errors** : Displays fitting errors.
	- **RMS** : The root-mean-squared distance between target and fitted 
        mesh points.
	- **Mean** : The mean distance between target and fitted mesh 
        points.
	- **S.D.** : The standard deviation of distances between target and 
        fitted mesh points.
- **Screeshot** : Save a screenshot of the current 3-D scene to file.
	- **Pixels X** : Width in pixels of the output image.
	- **Pixels Y** : Height in pixels of the output image.
	- **Filename** : Path of the output image file. File format is 
        defined by the suffix of the given filename.
	- **Save Screenshot** : Take screenshot and write to file.
	
Usage Notes
-----------
This step provides fine-scale fitting of a Fieldwork mesh to a target 
pointcloud (e.g. surface vertices from a segmented STL file). This step 
is typically used after a coarse registration step such as Fieldwork PC 
Mesh Fitting Step or Fieldwork Host-mesh Fitting Step. The mesh must be 
close to the target pointcloud for a reliable fit.

The registration is performed by an iterative least-squares optimisation 
of input mesh nodal coordinates P that mininimises

e = e_d(P) + w_ss\*e_s(P) + w_n\*e_n(P)

where e_d is the squared distance between points sampled on the input 
mesh and target points; e_s is the Sobelov penalty term that penalises 
against high curvature in the input mesh; and e_n is the element normal 
penalty term that penalises against non-continuous normals across 
element boundaries in the input mesh. Relaxing the weightings of the 
penalty terms will produce a closer fit of the mesh at the expense of 
mesh quality.

The accuracy of e_d(P) is affected by the mesh discretisation. A higher
discretisation means e_d(P) will be a more accurate representation of 
the distance between the continuous mesh surface and target points. 
However, higher discretisation will also result in longer fitting times.


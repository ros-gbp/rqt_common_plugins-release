Name:           ros-indigo-rqt-py-common
Version:        0.3.12
Release:        0%{?dist}
Summary:        ROS rqt_py_common package

Group:          Development/Libraries
License:        BSD
URL:            http://ros.org/wiki/rqt_py_common
Source0:        %{name}-%{version}.tar.gz

BuildArch:      noarch

Requires:       ros-indigo-actionlib
Requires:       ros-indigo-genpy
Requires:       ros-indigo-qt-gui
Requires:       ros-indigo-rosbag
Requires:       ros-indigo-roslib
Requires:       ros-indigo-rospy
Requires:       ros-indigo-rostopic
BuildRequires:  ros-indigo-catkin

%description
rqt_py_common provides common functionality for rqt plugins written in Python.
Despite no plugin is provided, this package is part of the rqt_common_plugins
repository to keep refactoring generic functionality from these common plugins
into this package as easy as possible. Functionality included in this package
should cover generic ROS concepts and should not introduce any special
dependencies beside &quot;ros_base&quot;.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/indigo" \
        -DCMAKE_PREFIX_PATH="/opt/ros/indigo" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/indigo

%changelog
* Fri Jul 24 2015 Dorian Scholz <scholz@sim.tu-darmstadt.de> - 0.3.12-0
- Autogenerated by Bloom

* Sat May 02 2015 Dorian Scholz <scholz@sim.tu-darmstadt.de> - 0.3.11-0
- Autogenerated by Bloom

* Wed Oct 01 2014 Dorian Scholz <scholz@sim.tu-darmstadt.de> - 0.3.10-0
- Autogenerated by Bloom

* Mon Aug 18 2014 Dorian Scholz <scholz@sim.tu-darmstadt.de> - 0.3.9-0
- Autogenerated by Bloom


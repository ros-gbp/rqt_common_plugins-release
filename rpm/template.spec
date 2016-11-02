Name:           ros-kinetic-rqt-py-common
Version:        0.4.3
Release:        0%{?dist}
Summary:        ROS rqt_py_common package

Group:          Development/Libraries
License:        BSD
URL:            http://ros.org/wiki/rqt_py_common
Source0:        %{name}-%{version}.tar.gz

BuildArch:      noarch

Requires:       ros-kinetic-actionlib
Requires:       ros-kinetic-genpy
Requires:       ros-kinetic-python-qt-binding >= 0.2.19
Requires:       ros-kinetic-qt-gui
Requires:       ros-kinetic-rosbag
Requires:       ros-kinetic-roslib
Requires:       ros-kinetic-rospy
Requires:       ros-kinetic-rostopic
BuildRequires:  ros-kinetic-catkin
BuildRequires:  ros-kinetic-genmsg
BuildRequires:  ros-kinetic-std-msgs

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
if [ -f "/opt/ros/kinetic/setup.sh" ]; then . "/opt/ros/kinetic/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/kinetic" \
        -DCMAKE_PREFIX_PATH="/opt/ros/kinetic" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/kinetic/setup.sh" ]; then . "/opt/ros/kinetic/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/kinetic

%changelog
* Wed Nov 02 2016 Dorian Scholz <scholz@sim.tu-darmstadt.de> - 0.4.3-0
- Autogenerated by Bloom

* Mon Sep 19 2016 Dorian Scholz <scholz@sim.tu-darmstadt.de> - 0.4.2-0
- Autogenerated by Bloom

* Mon May 16 2016 Dorian Scholz <scholz@sim.tu-darmstadt.de> - 0.4.1-0
- Autogenerated by Bloom

* Fri Apr 29 2016 Dorian Scholz <scholz@sim.tu-darmstadt.de> - 0.4.0-1
- Autogenerated by Bloom

* Wed Apr 27 2016 Dorian Scholz <scholz@sim.tu-darmstadt.de> - 0.4.0-0
- Autogenerated by Bloom


Name:           ros-indigo-rqt-topic
Version:        0.4.4
Release:        0%{?dist}
Summary:        ROS rqt_topic package

Group:          Development/Libraries
License:        BSD
URL:            http://ros.org/wiki/rqt_topic
Source0:        %{name}-%{version}.tar.gz

BuildArch:      noarch

Requires:       python-rospkg
Requires:       ros-indigo-python-qt-binding >= 0.2.19
Requires:       ros-indigo-rostopic
Requires:       ros-indigo-rqt-gui
Requires:       ros-indigo-rqt-gui-py
Requires:       ros-indigo-std-msgs
BuildRequires:  ros-indigo-catkin

%description
rqt_topic provides a GUI plugin for displaying debug information about ROS
topics including publishers, subscribers, publishing rate, and ROS Messages.

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
        -DCMAKE_INSTALL_LIBDIR="lib" \
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
* Fri Jan 27 2017 Dorian Scholz <scholz@sim.tu-darmstadt.de> - 0.4.4-0
- Autogenerated by Bloom

* Wed Nov 02 2016 Dorian Scholz <scholz@sim.tu-darmstadt.de> - 0.4.3-0
- Autogenerated by Bloom

* Tue Mar 08 2016 Dorian Scholz <scholz@sim.tu-darmstadt.de> - 0.3.13-0
- Autogenerated by Bloom

* Fri Jul 24 2015 Dorian Scholz <scholz@sim.tu-darmstadt.de> - 0.3.12-0
- Autogenerated by Bloom

* Sat May 02 2015 Dorian Scholz <scholz@sim.tu-darmstadt.de> - 0.3.11-0
- Autogenerated by Bloom


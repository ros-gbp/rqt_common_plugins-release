Name:           ros-indigo-rqt-dep
Version:        0.3.9
Release:        0%{?dist}
Summary:        ROS rqt_dep package

Group:          Development/Libraries
License:        BSD
URL:            http://ros.org/wiki/rqt_dep
Source0:        %{name}-%{version}.tar.gz

BuildArch:      noarch

Requires:       python-rospkg
Requires:       ros-indigo-qt-dotgraph
Requires:       ros-indigo-qt-gui
Requires:       ros-indigo-qt-gui-py-common
Requires:       ros-indigo-rqt-graph
Requires:       ros-indigo-rqt-gui-py
BuildRequires:  python-mock
BuildRequires:  ros-indigo-catkin

%description
rqt_dep provides a GUI plugin for visualizing the ROS dependency graph.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
mkdir -p build && cd build
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
cd build
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/indigo

%changelog
* Mon Aug 18 2014 Aaron Blasdel <ablasdel@gmail.com> - 0.3.9-0
- Autogenerated by Bloom


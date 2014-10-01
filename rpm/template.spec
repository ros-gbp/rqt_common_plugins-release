Name:           ros-indigo-rqt-reconfigure
Version:        0.3.10
Release:        0%{?dist}
Summary:        ROS rqt_reconfigure package

Group:          Development/Libraries
License:        BSD
URL:            http://ros.org/wiki/rqt_reconfigure
Source0:        %{name}-%{version}.tar.gz

BuildArch:      noarch

Requires:       ros-indigo-dynamic-reconfigure
Requires:       ros-indigo-rospy
Requires:       ros-indigo-rqt-console
Requires:       ros-indigo-rqt-gui
Requires:       ros-indigo-rqt-gui-py
Requires:       ros-indigo-rqt-py-common
BuildRequires:  ros-indigo-catkin

%description
This rqt plugin succeeds former dynamic_reconfigure's GUI (reconfigure_gui), and
provides the way to view and edit the parameters that are accessible via
dynamic_reconfigure. (12/27/2012) In the future, arbitrary parameters that are
not associated with any nodes (which are not handled by dynamic_reconfigure)
might become handled. However, currently as the name indicates, this pkg solely
is dependent on dynamic_reconfigure that allows access to only those params
latched to nodes.

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
* Wed Oct 01 2014 Scott K Logan <logans@cottsay.net> - 0.3.10-0
- Autogenerated by Bloom

* Mon Aug 18 2014 Scott K Logan <logans@cottsay.net> - 0.3.9-0
- Autogenerated by Bloom


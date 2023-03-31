%define apiver 3.2

Name:           kexi
Epoch:          16
#koffice has epoch 15. We need a higher epoch
Version: 3.2.0
Release:        2
Summary:        An integrated environment for managing data
Group:          Graphical desktop/KDE
License:        GPLv2+
URL:            http://www.kexi-project.org/
Source0:        http://download.kde.org/stable/%{name}/src/%{name}-%{version}.tar.xz
Patch0:		kexi-3.2.0-compile.patch

BuildRequires:  cmake(ECM)
BuildRequires:  breeze-icons

BuildRequires:  mariadb-devel
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(libpq) >= 9.6
BuildRequires:  pkgconfig(sqlite3)

BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5Help)
BuildRequires:  pkgconfig(Qt5Network)
BuildRequires:  pkgconfig(Qt5PrintSupport)
BuildRequires:  pkgconfig(Qt5Test)
BuildRequires:  pkgconfig(Qt5UiTools)
BuildRequires:  pkgconfig(Qt5WebKit)
BuildRequires:  pkgconfig(Qt5WebKitWidgets)
BuildRequires:  pkgconfig(Qt5Widgets)
BuildRequires:  pkgconfig(Qt5Xml)

BuildRequires:  cmake(KF5Archive)
BuildRequires:  cmake(KF5Codecs)
BuildRequires:  cmake(KF5Completion)
BuildRequires:  cmake(KF5Config)
BuildRequires:  cmake(KF5ConfigWidgets)
BuildRequires:  cmake(KF5CoreAddons)
BuildRequires:  cmake(KF5GuiAddons)
BuildRequires:  cmake(KF5I18n)
BuildRequires:  cmake(KF5IconThemes)
BuildRequires:  cmake(KF5ItemViews)
BuildRequires:  cmake(KF5KIO)
BuildRequires:  cmake(KF5TextEditor)
BuildRequires:  cmake(KF5TextWidgets)
BuildRequires:  cmake(KF5WidgetsAddons)
BuildRequires:  cmake(KF5XmlGui)
BuildRequires:  cmake(KF5Crash)
BuildRequires:  cmake(KF5Parts)

BuildRequires:  cmake(KDb) >= %{version}
BuildRequires:  cmake(KReport) >= %{version}
BuildRequires:  cmake(KPropertyWidgets) >= %{version}
BuildRequires:  cmake(Marble)

Requires:       kdb >= %{version}
# needed for local databases
Requires:	kdb-sqlite
Requires:       kproperty >= %{version}
Requires:       kreport >= %{version}

Conflicts:      calligra-core < 3.0-1
%rename	calligra-kexi

%define obsoletelibs kexiutils kexiundo kexicore kexiguiutils kexiextendedwidgets kexidataviewcommon kexirelationsview keximigrate keximain kexidatatable kexiformutils kformdesigner
%{expand:%(for lib in %{obsoletelibs}; do echo Obsoletes: %%mklibname $lib 15; echo; done)}


%description
Kexi is an integrated data management application.
It can be used for creating database schemas, inserting data, performing
queries, and processing data. Forms can be created to provide a custom 
interface to your data. All database objects – tables, queries 
and forms – are stored in the database, making it easy to share 
data and design.

%files -f %{name}.lang
%doc COPYING*
%{_kde5_bindir}/%{name}-%apiver
%{_qt5_plugindir}/%{name}/
%{_kde5_datadir}/%{name}/
%{_datadir}/metainfo/org.kde.%{name}-%{apiver}.appdata.xml
%{_kde5_applicationsdir}/org.kde.%{name}-%{apiver}.desktop
%{_datadir}/icons/*/*/*/kexi*.*

#--------------------------------------------------------------------

%define libkexicore_major 3.2
%define libkexicore %mklibname kexicore %{apiver} %libkexicore_major

%package -n     %libkexicore
Summary:        Kexi core library
Group:          System/Libraries

%description -n %libkexicore
Kexi core library.

%files -n %libkexicore
%{_kde5_libdir}/libkexicore%{apiver}.so.%{libkexicore_major}*

#--------------------------------------------------------------------

%define libkexidatatable_major 3.2
%define libkexidatatable %mklibname kexidatatable %apiver %libkexidatatable_major

%package -n     %libkexidatatable
Summary:        Kexi data table library
Group:          System/Libraries

%description -n %libkexidatatable
Kexi data table library.

%files -n %libkexidatatable
%{_kde5_libdir}/libkexidatatable%{apiver}.so.%{libkexidatatable_major}*

#--------------------------------------------------------------------

%define libkexidataviewcommon_major 3.2
%define libkexidataviewcommon %mklibname kexidataviewcommon %apiver %libkexidataviewcommon_major

%package -n     %libkexidataviewcommon
Summary:        Kexi data view common library
Group:          System/Libraries

%description -n %libkexidataviewcommon
Kexi data view common library.

%files -n %libkexidataviewcommon
%{_kde5_libdir}/libkexidataviewcommon%{apiver}.so.%{libkexidataviewcommon_major}*

#-------------------------------------------------------------------- 

%define libkexiextendedwidgets_major 3.2
%define libkexiextendedwidgets %mklibname kexiextendedwidgets %apiver %libkexiextendedwidgets_major

%package -n     %libkexiextendedwidgets
Summary:        Kexi extended widgets library
Group:          System/Libraries

%description -n %libkexiextendedwidgets
Kexi extended widgets library.

%files -n %libkexiextendedwidgets
%{_kde5_libdir}/libkexiextendedwidgets%{apiver}.so.%{libkexiextendedwidgets_major}*

#--------------------------------------------------------------------

%define libkexiformutils_major 3.2
%define libkexiformutils %mklibname kexiformutils %apiver %libkexiformutils_major

%package -n     %libkexiformutils
Summary:        Kexi formutils library
Group:          System/Libraries

%description -n %libkexiformutils
Kexi formutils library.

%files -n %libkexiformutils
%{_kde5_libdir}/libkexiformutils%{apiver}.so.%{libkexiformutils_major}*

#--------------------------------------------------------------------

%define libkexiguiutils_major 3.2
%define libkexiguiutils %mklibname kexiguiutils %apiver %libkexiguiutils_major

%package -n     %libkexiguiutils
Summary:        Kexi gui utils library
Group:          System/Libraries

%description -n %libkexiguiutils
Kexi gui utils library.

%files -n %libkexiguiutils
%{_kde5_libdir}/libkexiguiutils%{apiver}.so.%{libkexiguiutils_major}*

#--------------------------------------------------------------------

%define libkeximain_major 3.2
%define libkeximain %mklibname keximain %{apiver} %libkeximain_major

%package -n     %libkeximain
Summary:        Kexi main library
Group:          System/Libraries

%description -n %libkeximain
Kexi main library.

%files -n %libkeximain
%{_kde5_libdir}/libkeximain%{apiver}.so.%{libkeximain_major}*

#--------------------------------------------------------------------

%define libkeximigrate_major 3.2
%define libkeximigrate %mklibname keximigrate %{apiver} %libkeximigrate_major

%package -n     %libkeximigrate
Summary:        Kexi migrate library
Group:          System/Libraries

%description -n %libkeximigrate
Kexi migrate library.

%files -n %libkeximigrate
%{_kde5_libdir}/libkeximigrate%{apiver}.so.%{libkeximigrate_major}*

#--------------------------------------------------------------------

%define libkexirelationsview_major 3.2
%define libkexirelationsview %mklibname kexirelationsview %{apiver} %libkexirelationsview_major

%package -n     %libkexirelationsview
Summary:        Kexi relations view library
Group:          System/Libraries

%description -n %libkexirelationsview
Kexi relations view library.

%files -n %libkexirelationsview
%{_kde5_libdir}/libkexirelationsview%{apiver}.so.%{libkexirelationsview_major}*

#--------------------------------------------------------------------

%define libkexiundo_major 3.2
%define libkexiundo %mklibname kexiundo %{apiver} %libkexiundo_major

%package -n     %libkexiundo
Summary:        Kexi undo library
Group:          System/Libraries

%description -n %libkexiundo
Kexi undo library.

%files -n %libkexiundo
%{_kde5_libdir}/libkexiundo%{apiver}.so.%{libkexiundo_major}*

#--------------------------------------------------------------------

%define libkexiutils_major 3.2
%define libkexiutils %mklibname kexiutils %{apiver} %libkexiutils_major

%package -n     %libkexiutils
Summary:        Kexi utils library
Group:          System/Libraries

%description -n %libkexiutils
Kexi utils library.

%files -n %libkexiutils
%{_kde5_libdir}/libkexiutils%{apiver}.so.%{libkexiutils_major}*

#--------------------------------------------------------------------

%define libkformdesigner_major 3.2
%define libkformdesigner %mklibname kformdesigner %apiver %libkformdesigner_major

%package -n     %libkformdesigner
Summary:        Kexi form designer library
Group:          System/Libraries

%description -n %libkformdesigner
Kexi form designer library.

%files -n %libkformdesigner
%{_kde5_libdir}/libkformdesigner%{apiver}.so.%{libkformdesigner_major}*

#--------------------------------------------------------------------

%define kexi_devel %mklibname %{name} -d

%package -n     %kexi_devel
Summary:        Development files for %{name}
Group:          Development/KDE and Qt
Requires:       %libkexicore = %epoch:%version-%release
Requires:       %libkexidatatable = %epoch:%version-%release
Requires:       %libkexidataviewcommon = %epoch:%version-%release
Requires:       %libkexiextendedwidgets = %epoch:%version-%release
Requires:       %libkexiformutils = %epoch:%version-%release
Requires:       %libkexiguiutils = %epoch:%version-%release
Requires:       %libkeximain = %epoch:%version-%release
Requires:       %libkeximigrate = %epoch:%version-%release
Requires:       %libkexirelationsview = %epoch:%version-%release
Requires:       %libkexiundo = %epoch:%version-%release
Requires:       %libkexiutils = %epoch:%version-%release
Requires:       %libkformdesigner = %epoch:%version-%release
Provides:       %name-devel = %epoch:%version-%release

%description -n %kexi_devel
The %{kexi_devel} package contains libraries and header files for
developing applications that use %{name}.

%files -n %kexi_devel
%{_kde5_libdir}/*.so

#--------------------------------------------------------------------

%prep
%autosetup -p1

%build
%cmake_kde5
%ninja

%install
%ninja_install -C build

%find_lang %{name} --all-name --with-kde

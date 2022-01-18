%global modname tqdm
%global srcname %{modname}

Name:           python-%{modname}
Version:        4.62.3
Release:        %autorelease
Summary:        Fast, Extensible Progress Meter

# see PACKAGE-LICENSING for more info
License:        MPLv2.0 and MIT
URL:            https://github.com/tqdm/tqdm
Source0:        %{pypi_source}

BuildArch:      noarch

%global _description \
tqdm (read taqadum, تقدّم) means "progress" in Arabic.\
\
Instantly make your loops show a smart progress meter - just wrap any iterable\
with "tqdm(iterable)", and you are done!

%description %{_description}

%package -n python3-%{modname}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{modname}}
BuildRequires:  python3-devel

# tox.ini contains coverage and unpackaged dependencies (nbval)
BuildRequires:  python3-pytest
BuildRequires:  python3-pytest-asyncio
BuildRequires:  python3-pytest-timeout

# optional test deps
BuildRequires:  python3-tkinter
BuildRequires:  python3-dask
BuildRequires:  python3-numpy
BuildRequires:  python3-pandas
BuildRequires:  python3-rich
#BuildRequires:  python3-keras -- not available

%description -n python3-%{modname} %{_description}

Python 3 version.

%prep
%autosetup -n %{modname}-%{version}
chmod -x tqdm/completion.sh

# https://github.com/tqdm/tqdm/pull/1292
echo 'include tqdm/tqdm.1' >> MANIFEST.in
echo 'include tqdm/completion.sh' >> MANIFEST.in


%generate_buildrequires
%pyproject_buildrequires -r

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{modname}
install -Dpm0644 \
  %{buildroot}%{python3_sitelib}/tqdm/tqdm.1 \
  %{buildroot}%{_mandir}/man1/tqdm.1
install -Dpm0644 \
  %{buildroot}%{python3_sitelib}/tqdm/completion.sh \
  %{buildroot}%{_datadir}/bash-completion/completions/tqdm.bash

%check
%pytest

%files -n python3-%{modname} -f %{pyproject_files}
%license LICENCE
%doc README.rst examples
%{_bindir}/tqdm
%{_mandir}/man1/tqdm.1*
%dir %{_datadir}/bash-completion
%dir %{_datadir}/bash-completion/completions
%{_datadir}/bash-completion/completions/tqdm.bash

%changelog
%autochangelog

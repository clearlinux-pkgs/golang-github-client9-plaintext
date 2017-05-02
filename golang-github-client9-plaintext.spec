Name     : golang-github-client9-plaintext
Version  : 444b7b59bff6d01d5ea57a9d30884b7d7584a964
Release  : 3
URL      : https://github.com/client9/plaintext/archive/444b7b59bff6d01d5ea57a9d30884b7d7584a964.tar.gz
Source0  : https://github.com/client9/plaintext/archive/444b7b59bff6d01d5ea57a9d30884b7d7584a964.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : MIT
BuildRequires : go
BuildRequires : golang-googlecode-go-net

%description
# plaintext
[![Build Status](https://travis-ci.org/client9/plaintext.svg?branch=master)](https://travis-ci.org/client9/plaintext) [![Go Report Card](http://goreportcard.com/badge/client9/plaintext)](http://goreportcard.com/report/client9/plaintext) [![GoDoc](https://godoc.org/github.com/client9/plaintext?status.svg)](https://godoc.org/github.com/client9/plaintext) [![Coverage](http://gocover.io/_badge/github.com/client9/plaintext)](http://gocover.io/github.com/client9/plaintext) [![license](https://img.shields.io/badge/license-MIT-blue.svg?style=flat)](https://raw.githubusercontent.com/client9/plaintext/master/LICENSE)

%prep
%setup -q -n plaintext-444b7b59bff6d01d5ea57a9d30884b7d7584a964

%build
export LANG=C


%install
rm -rf %{buildroot}
%global gopath /usr/lib/golang
%global library_path github.com/client9/plaintext

# Copy all *.go and *.s files
install -d -p %{buildroot}%{gopath}/src/%{library_path}/
for ext in go s src golden template; do
    for file in $(find . -iname "*.$ext") ; do
         install -d -p %{buildroot}%{gopath}/src/%{library_path}/$(dirname $file)
         cp -pav $file %{buildroot}%{gopath}/src/%{library_path}/$file
    done
done

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost
export GOPATH=%{buildroot}%{gopath}
go test %{library_path}/... || :

%files
%defattr(-,root,root,-)
/usr/lib/golang/src/github.com/client9/plaintext/cmd/plaintext/main.go
/usr/lib/golang/src/github.com/client9/plaintext/golang.go
/usr/lib/golang/src/github.com/client9/plaintext/html.go
/usr/lib/golang/src/github.com/client9/plaintext/html_test.go
/usr/lib/golang/src/github.com/client9/plaintext/identity.go
/usr/lib/golang/src/github.com/client9/plaintext/identity_test.go
/usr/lib/golang/src/github.com/client9/plaintext/markdown.go
/usr/lib/golang/src/github.com/client9/plaintext/markdown_test.go
/usr/lib/golang/src/github.com/client9/plaintext/mime.go
/usr/lib/golang/src/github.com/client9/plaintext/script.go
/usr/lib/golang/src/github.com/client9/plaintext/script_test.go
/usr/lib/golang/src/github.com/client9/plaintext/template.go
/usr/lib/golang/src/github.com/client9/plaintext/template_test.go
/usr/lib/golang/src/github.com/client9/plaintext/text.go

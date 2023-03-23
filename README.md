# README #

This repo will contain dockerised standardized development environments.

### What is this repository for? ###

* DarbTech internal use of Odoo-12 Open Source development
* 1.0 beta


### How do I get set up? ###

* Deployed service is accessible under port 9269

### Contribution guidelines ###

* Writing tests
* Code review
* Other guidelines
	Follow darbtech git flow then make a merge request

### How to manually update module ###

```console
docker-compose exec -u odoo web bash
/entrypoint.sh odoo --no-http --stop-after-init --update module_name
```

### Who do I talk to? ###

* Repo owner or admin: Stéphane DAGUET - stephane@darbtech.net

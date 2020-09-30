# syntheticapi.py

syntheticapi.py is supplied to offer a simple API to Instana's configuration.yaml, focussed on adding and removing monitored entities for Instana's synthetic ping.

  
# Background

At the moment, the way of configuring external synthetic monitoring for Instana is via an agent configuration file. This of course does not lend well to automation - and whilst gitops can enable simple distribution, there is still the issue of automating the initial file field population.

  
The original configuration.yaml can be left intact, and used for other purposes, whilst we will implement a chained configuration in the repo called configuration-sythetics.yaml.

This will get automatically parsed every 60 seconds. and leading to an agent log file looking something like this:-

  

    2020-09-30T11:13:15.743+0100 | INFO | a-config-service | PluginConfigurationFilesImpl | 51 - com.instana.agent - 1.1.572 | Parsed configuration file /opt/instana/agent/etc/instana/configuration-synthetics.yaml

  
# Prerequisites

  
 - A machine running the Instana agent. For synthetic tests, its usually
   preferable to run a dedicated small VM for this.    
 - Python 3.x
 - Pip

 
# Modules

Pip Modules :

- pyyaml
- flask

 
# Installation

- Copy the syntheticapi.py file to the Instana configuration directory

- Run the file 'python3 syntheticapi.py' by your preferred method

- The flask process will listen on port 5000, on 0.0.0.0, though this can be modified in code.

  
**POST**

Takes parameters as string values.

    type : http or icmp
    
    target: address (eg https:\\www.microsoft.com)
    
    label: Site label (Needs to be unique)

**Curl Example:-**

    curl -X "POST" "http://192.168.13.250:5000/api/synthetics?type=http&target=https:%2F%2Fwww.microsoft.com%2Fen-gb%2F&label=microsoft"

**GET**

Returns all configured endpoints.Useful for testing

Curl Example:-

    curl "http://192.168.13.250:5000/api/synthetics"

**DELETE**

Takes parameters:

    label: Site Label


Curl Example:-

    curl -X "DELETE" "http://192.168.13.250:5000/api/synthetics?label=Justyns_Server"


# Caveats.

 - There is very little error checking.But well, its simple.
   
  - Label is the unique key, and is case sensitive
   
  - No security, but really intended to run internally. Could easily be modified to create a master configuration that could be externally distributed via Instana's GitOps.

# configuration-synthetics.yaml Format (for information)

    com.instana.plugin.ping:
    
    endpoints:
    
    sample:
    
    target: http://172.16.0.42:80/health
    
    type: http
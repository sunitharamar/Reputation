
 

# Deliverables:

Scrape list of doctors at Kaiser Permanente, Northern California Region within the 

Redwood City Office.
https://healthy.kaiserpermanente.org/northern-california/doctors-locations#/search-result

 


# Description:

Please write a scraper with which you can scrape the following details. Get at least 50 Physician with following details. Show the code and implementation details.

Physician Name: Stella Sarang Abhyankar, MD

Physician Specialty: Hospital Medicine

Practicing Address:

    Redwood City Medical Center
    1150 Veterans Blvd 
    Redwood City, CA 94063
    
Phone: 650-299-2000
 
 
 


```python
!pip install splinter
```

    Requirement already satisfied: splinter in /Users/sunitharamakrishnan/anaconda3/envs/PythonData/lib/python3.6/site-packages
    Requirement already satisfied: selenium>=3.4.3 in /Users/sunitharamakrishnan/anaconda3/envs/PythonData/lib/python3.6/site-packages (from splinter)



```python
# Dependencies

# https://splinter.readthedocs.io/en/latest/drivers/chrome.html
from selenium import webdriver
from splinter import Browser
from bs4 import BeautifulSoup  
import requests
import tweepy
import yaml
import pandas as pd
import time
import re
import pymongo
```


```python
#driver = webdriver.Chrome('/path/to/chromedriver') 
executable_path = {'executable_path': '/usr/local/bin/chromedriver'}
browser = Browser('chrome', **executable_path, headless=False)
```


```python
# Scrape the Kaiser Redwood city office site in northern california. 
kaiser_url = "https://healthy.kaiserpermanente.org/northern-california/doctors-locations#/search-form"  
response = requests.get(kaiser_url)

# Create BeautifulSoup object; parse with 'html.parser'
soup = BeautifulSoup(response.text, 'html.parser')

# To understand the data before collecting from the web.
print(soup.prettify())

 
```

    <!DOCTYPE HTML>
    <html lang="en-US">
     <head>
      <meta charset="utf-8"/>
      <meta content="IE=edge, chrome=1" http-equiv="X-UA-Compatible"/>
      <meta content="width=device-width, initial-scale=1.0" name="viewport"/>
      <meta name="keywords">
       <!-- Meta tags Override for SEO purposes-->
       <title>
        Find Doctors and Locations
       </title>
       <meta name="description">
        <script data-dtconfig="featureHash=2SVfghjqrtx|md=2=a[name='DCSExt.guid']@content,1=csoguid|lastModification=1521847396477|dtVersion=10131171206150117|tp=500,50,0,1|agentUri=/etc/designs/ruxitagentjs_2SVfghjqrtx_10131171206150117.js|reportUrl=/etc/designs/rb_ea96fd35-4a91-4571-9999-391fba61c917|rid=RID_1372737073|rpid=484316002|domain=kaiserpermanente.org" src="/etc/designs/ruxitagentjs_2SVfghjqrtx_10131171206150117.js" type="text/javascript">
        </script>
        <link href="https://healthy.kaiserpermanente.org/northern-california/doctors-locations" rel="canonical"/>
        <meta content="text/html; charset=utf-8" http-equiv="content-type"/>
        <meta content="on" http-equiv="x-dns-prefetch-control"/>
        <link href="https://assets.adobedtm.com" rel="dns-prefetch"/>
        <link href="https://cdn.tt.omtrdc.net" rel="dns-prefetch"/>
        <link href="https://kaiser.demdex.net" rel="dns-prefetch"/>
        <link href="https://kaiser.tt.omtrdc.net" rel="dns-prefetch"/>
        <link href="https://smetrics.kaiserpermanente.org" rel="dns-prefetch"/>
        <link href="https://statse.webtrendslive.com" rel="dns-prefetch"/>
        <link href="https://s.webtrends.com" rel="dns-prefetch"/>
        <meta content="en_US" property="og:locale">
         <meta content="article" property="og:type">
          <meta content="yes" property="searchable">
           <link href="/etc/designs/kporg/kp-foundation/clientlib-structural/assets/images/favicon-16x16.png" rel="icon" type="image/x-icon">
            <script type="text/javascript">
             (function() {
                    window.ContextHub = window.ContextHub || {};
    
                    /* setting paths */
                    ContextHub.Paths = ContextHub.Paths || {};
                    ContextHub.Paths.CONTEXTHUB_PATH = "/etc/cloudsettings/default/contexthub";
                    ContextHub.Paths.RESOURCE_PATH = "\/content\/kporg\/en\/northern\u002Dcalifornia\/doctors\u002Dlocations\/jcr:content\/contexthub";
                    ContextHub.Paths.SEGMENTATION_PATH = "\/etc\/segmentation\/contexthub";
                    ContextHub.Paths.CQ_CONTEXT_PATH = "";
    
                    /* setting initial constants */
                    ContextHub.Constants = ContextHub.Constants || {};
                    ContextHub.Constants.ANONYMOUS_HOME = "/home/users/P/PQt0CSm4uzgDa-vRmuW7";
                    ContextHub.Constants.MODE = "no-ui";
                }());
            </script>
            <script src="/etc/cloudsettings/default/contexthub.kernel.js" type="text/javascript">
            </script>
            <script type="text/javascript">
             if ( !window.CQ_Analytics ) {
                    window.CQ_Analytics = {};
                }
                if ( !CQ_Analytics.TestTarget ) {
                    CQ_Analytics.TestTarget = {};
                }
                CQ_Analytics.TestTarget.clientCode = 'kaiser';
            </script>
            <script src="/etc/clientlibs/foundation/testandtarget/parameters.f294c144a1d384b83dcadb0963f00cd6.js" type="text/javascript">
            </script>
            <script src="/etc/clientlibs/foundation/testandtarget/atjs-integration.8cf8854620a39e7a022f382074264a15.js" type="text/javascript">
            </script>
            <script>
             var jsonConfigs = {
            "global": JSON.parse("{\n  \x22keepAliveComponentName\x22: \x22Keep Alive Component\x22,\n  \x22configUrl\x22: \x22\/config\u002Djson\/kp\u002Dfoundation.json\x22,\n  \x22userProfileFeature\x22: \x22all\x22,\n  \x22entitlementsApiUri\x22: \x22\/mycare\/v2.0\/entitlements\x22,\n  \x22api.keepalive.timeout\x22: 3000,\n  \x22apiKey\x22: \x22kprwd19696894446387888128\x22,\n  \x22appName\x22: \x22AEM\x22,\n  \x22entitlementsComponentName\x22: \x22Entitlements Component\x22,\n  \x22careUserApiUri\x22: \x22\/care\/v1.0\/user\x22,\n  \x22apipApiUrl\x22: \x22https:\/\/apip.kaiserpermanente.org\x22,\n  \x22userComponentName\x22: \x22User Profile Component\x22,\n  \x22proxyComponentName\x22: \x22Proxy Component\x22,\n  \x22mycareUserApiUri\x22: \x22\/mycare\/v1.0\/user\x22,\n  \x22apiUrl\x22: \x22https:\/\/healthy.kaiserpermanente.org\x22,\n  \x22proxyApiUri\x22: \x22\/mycare\/v2.0\/proxyinformation\x22,\n  \x22jsonHash\x22: \x225df8cf682b7df41f98768bcc42ace1c8\x22,\n  \x22createProxyApiUri\x22: \x22\/mycare\/v2.0\/createproxyaccount\x22,\n  \x22proxyNoCacheApiUri\x22: \x22\/mycare\/v2.1\/proxyinformation\x22,\n  \x22userNameApiUri\x22: \x22\/mycare\/v1.0\/username\x22,\n  \x22memberDataApiUri\x22: \x22\/mycare\/membership\/v1.0\/account\x22,\n  \x22pictureDataHeroImage\x22: [\n    {\n      \x22extension\x22: \x22\u002Dmobile\x22,\n      \x22media\u002Dstring\x22: \x22(max\u002Dwidth: 599px)\x22\n    },\n    {\n      \x22extension\x22: \x22\u002Dtablet\x22,\n      \x22media\u002Dstring\x22: \x22(max\u002Dwidth: 767px)\x22\n    },\n    {\n      \x22extension\x22: \x22\u002Ds\u002Ddt\x22,\n      \x22media\u002Dstring\x22: \x22(max\u002Dwidth: 1023px)\x22\n    },\n    {\n      \x22extension\x22: \x22\u002Dm\u002Ddt\x22,\n      \x22media\u002Dstring\x22: \x22(max\u002Dwidth: 1279px)\x22\n    },\n    {\n      \x22extension\x22: \x22\u002Dl\u002Ddt\x22\n    }\n  ],\n  \x22componentName\x22: \x22KP Foundation\x22,\n  \x22auditLogApiUri\x22: \x22\/mycare\/event\/event\u002Dhandler\/v1.0\/auditLog\x22,\n  \x22googleClientKey\x22: \x22gme\u002Dkaiserfoundation\x22\n}")
        };
        jsonConfigs.global.appName = "kp\u002Dfoundation";
        if(true) {
            jsonConfigs.feature = JSON.parse("{\n  \x22apiKey\x22: \x22kprwdfdl83184977525379497984\x22,\n  \x22facZipSource\x22: \x22kp\u002Dmg\u002Dfacdir\u002Dproximity\x22,\n  \x22docSort\x22: \x22provider_sort last_name\x22,\n  \x22mgBinsFunction\x22: \x22xml\u002Dfeed\u002Ddisplay\u002Dwpp\u002Dmg\u002Dbins\x22,\n  \x22docZipSource\x22: \x22kp\u002Ddoctor\u002Dproximity\x22,\n  \x22timeout\x22: 60000,\n  \x22resultsPerPage\x22: 20,\n  \x22jsonHash\x22: \x22c48d91856a1c9fc49ad66518fae8a0c7\x22,\n  \x22maxResults\x22: 200,\n  \x22facSource\x22: \x22kp\u002Dmg\u002Dfacdir\u002Dkeyword\x22,\n  \x22enableLog\x22: true,\n  \x22searchUrl\x22: \x22\/fdl\/search\x22,\n  \x22facSort\x22: \x22affiliated_facility title\x22,\n  \x22docFilOrder\x22: [\n    \x22pcp_label\x22,\n    \x22island_label\x22,\n    \x22medical_specialty_label\x22,\n    \x22distance_label\x22,\n    \x22city_label\x22,\n    \x22health_plan_label\x22,\n    \x22provider_label\x22,\n    \x22gender_label\x22,\n    \x22dr_language_label\x22,\n    \x22hospital_label\x22\n  ],\n  \x22mgFunction\x22: \x22xml\u002Dfeed\u002Ddisplay\u002Dwpp\u002Dmg\x22,\n  \x22facFilOrder\x22: [\n    \x22island_label\x22,\n    \x22distance_label\x22,\n    \x22city_label\x22,\n    \x22hospital_affiliation_label\x22,\n    \x22department_type_label\x22,\n    \x22health_plan_label\x22,\n    \x22services_label\x22\n  ],\n  \x22contentMetaUrl\x22: \x22\/fdl\/contentmetadata\x22,\n  \x22signOnUrl\x22: \x22\/fdl\/token\x22,\n  \x22docSource\x22: \x22kp\u002Ddoctor\x22,\n  \x22contentUrl\x22: \x22\/fdl\/content\x22,\n  \x22regionUrl\x22: \x22regionlist.json\x22,\n  \x22distanceUrl\x22: \x22distancelist.json\x22,\n  \x22envName\x22: \x22prod\x22,\n  \x22docProject\x22: \x22kp\u002Ddoctor\u002Dproject\x22,\n  \x22facProject\x22: \x22kp\u002Dmg\u002Dfacdir\u002Dproject\x22\n}");
            jsonConfigs.feature.appName = "doctors\u002Dlocations";
        };
            </script>
            <link href="/etc/designs/kporg/kp-foundation/clientlib-all.d8f81d1c2cf0bf1516230c94af7264be.css" rel="stylesheet" type="text/css"/>
            <script src="/etc/clientlibs/granite/jquery.fb50358df4c2bd6aa6e1dd5b0d9b9d29.js" type="text/javascript">
            </script>
            <script src="/etc/designs/kporg/kp-foundation/clientlib-external.dece2601f9267e8f44c2036897d79cd1.js" type="text/javascript">
            </script>
            <script src="/etc/designs/kporg/kp-foundation/clientlib-modules/slick.298ad9d608920558ccb43ded8254d543.js" type="text/javascript">
            </script>
            <script src="/etc/designs/kporg/kp-foundation/clientlib-all.c8c519f16460c9d6a877610834c16adf.js" type="text/javascript">
            </script>
            <!-- loading configuration of load bff through the tml script tag. Specially GMO-->
            <script>
             if(window.jsonConfigs.feature)
    {
      console.log("If feature config exist condition is true. Check the loadBFFConfig object.")
      if(window.jsonConfigs.feature.loadBFFConfig)
      {
        console.log("If loadBFFConfig object exist go through this function..")
        // This script is going to run before headlibs-extra html.
        var preload = window.jsonConfigs.feature.loadBFFConfig;
    
        // Function to read the cookie.
        function getCookie(cname) {
            var name = cname + "=";
            var ca = document.cookie.split(';');
            for (var i = 0; i < ca.length; i++) {
                var c = ca[i];
                while (c.charAt(0) === ' ')
                    c = c.substring(1);
                if (c.indexOf(name) === 0)
                    return c.substring(name.length, c.length);
            }
            return ""; // Create var with empty string and assign.
        };
    
        // This condition is added to avoid the API call on aem edit mode.
        var aemEdit_Mode = getCookie("wcmmode");
    
        // if AEM edit/preview mode then we don't want to make the API call.
        if(aemEdit_Mode == 'preview' || aemEdit_Mode == 'edit')
        {
            console.log("If AEM edit mode then bypass the call.");
        }
        else
        {
            // Check if preload object is empty.
            if (typeof preload  != 'undefined' && preload)
            {
                if(preload != null && preload.length > 0)
                {
                  $kp.KPUserProfile.UserProfileClient.load().then(function(data){console.log('user data initialized')}, function(err){console.log(err)});
                  var appversion = navigator.appVersion;
    
                  //--- Logic to check proxyCookie is exist or not? -----
                  var isProxyCookiethere = false;
                  var proxyCookie = window.$kp.KPProxyPicker.ProxyPickerClient.getRelationshipId();
                  if(proxyCookie!='self')
                  {
                    isProxyCookiethere = true;
                  }
                  // If spanish domain then dev url is going to change.
                  // Specially AEM page.
                  var spanishLangPage = false;
                  var getLangVal = getCookie("kpLanguage");
                  if(getLangVal == "es-US")
                  {
                    spanishLangPage = true;
                  }
    
                  for (var i = 0; i < preload.length; i++)
                  {
                      preload[i]['headers']["X-osversion"] = appversion;
                      if(spanishLangPage && preload[i].es_domain)
                      {
                          preload[i]['url'] = preload[i]['es_domain']+preload[i]['uri'];
                      }
                      else
                      {
                          preload[i]['url'] = preload[i]['domain']+preload[i]['uri'];
                      }
    
                      // After construct the url remove domain and url.
                      delete preload[i]['domain'];
                      delete preload[i]['es_domain'];
                      delete preload[i]['uri'];
    
                      if(isProxyCookiethere)
                      {
                          preload[i]['headers']["X-relId"] = proxyCookie;
                      }
                      else
                      {
                        delete preload[i]['headers']["X-relId"];
                      }
                  }
                  // Making call to loadBFFAPIs.
                  $kp.KPClientCommons.WebUtil.loadBFFAPIs(preload);
              }
            }
            else
            {
                console.log("preload object is empty.");
            }
        }
      }
      else
      {
        console.log("loadBFFConfig objectis missing.")
      }
    }
    else
    {
      console.log("feature object is missing.")
    }
            </script>
            <link href="/etc/designs/kporg/doctors-locations/clientlib.81ed64144a7ccd4ad9cae176035640d2.css" rel="stylesheet" type="text/css"/>
            <script src="/etc/designs/kporg/kp-foundation/clientlib-modules/aem-target.5cfc2f73ec15e05c0fecdd42001c952f.js" type="text/javascript">
            </script>
            <script>
             var digitalData = {
    
        page : {
                pageInfo : {
                    pageName : "kporg:en:northern-california:doctors-locations"
                },
                category : {
                    primaryCategory : "kporg",
                    subCategory1 : "kporg:en",
                    subCategory2 : "kporg:en:northern\u002Dcalifornia",
                    subCategory3 : "kporg:en:northern\u002Dcalifornia:doctors\u002Dlocations",
                    subCategory4 : "",
                    subCategory5 : ""
                }
            },
            user : {
               profile : {
                },
                segment : {
                }
            },
            global : {
            	feature_name : "Find Doctors and Locations",
              guid : ""
            }
        }
            </script>
            <script src="//assets.adobedtm.com/41f6137a488e72eca8418be00135b2e51c0d0e27/satelliteLib-2bc610ca12e2f1708a709fe3c85c9a06e6f28e0f.js">
            </script>
           </link>
          </meta>
         </meta>
        </meta>
       </meta>
      </meta>
     </head>
     <body>
      <div aria-describedby="timeout-modal-description" aria-hidden="true" aria-labelledby="timeout-modal-title" class="global-modal-timeout timeout-warning kp-modal" data-element="Modal Appear" data-feature="Find Doctors and Locations" id="global-modal-timeout-id" role="dialog">
       <div class="modal-fade-screen">
        <div class="modal-inner" role="document" tabindex="-1">
         <p>
          <span class="screenreader-only" id="timeout-modal-title">
           Timeout Warning
          </span>
         </p>
         <div class="modal-header">
          <h4 class="page-heading timeout-modal-header">
           Want to stay signed on?
          </h4>
          <div>
          </div>
         </div>
         <div class="content" id="timeout-modal-description">
          If you haven't used your browser for more than 20 minutes, our system will automatically sign you off to protect your privacy.
          <br/>
          <br/>
          If you're filling in a form, you'll lose any information you haven't saved when we sign you off.
          <br/>
          <br/>
          Time remaining before sign off :
          <span class="countdown-timer">
          </span>
         </div>
         <div class="modal-buttons">
          <button class="button -action signoff-modal">
           Sign off
          </button>
          <button class="button -action -inverted ping-alive">
           Stay signed on
          </button>
         </div>
        </div>
       </div>
      </div>
      <a class="screenreader-only new-accessibility" href="/health/poc?uri=content%3Aancillary&amp;ctype=informational&amp;tid=WPP%3A%3ALXJZXQ4NU&amp;tname=site_context">
       New Accessibility Information
      </a>
      <div class="kp-global-header-component screen-only" data-analytics-location="kp-global-header">
       <div class="banner">
        <div class="alerts-notification-placeholder" data-uri="/northern-california/alerts/notification.partial.doctors-locations" id="alerts-notification-placeholder-id">
        </div>
       </div>
       <div data-uri="/northern-california/system/messages/gem/1005.data.json" id="proxy-error-placeholder-id">
       </div>
       <header class="kp-header blank" data-analytics-location="kp-header" data-header-state="LOGGED_OUT" data-keep-alive="obssobased" id="kp-header">
        <div class="top-header">
         <a class="kp-logo" data-analytics-click="kp-logo" data-analytics-type="image" href="/northern-california" id="accessCare">
          <div class="primary screen-only">
           <img alt="" class="logo-long" src="/etc/designs/kporg/kp-foundation/clientlib-structural/assets/images/logo.svg"/>
           <img alt="" class="logo-short" src="/etc/designs/kporg/kp-foundation/clientlib-structural/assets/images/kp-icon-mini.svg"/>
           <img alt="" class="logo-icon" src="/etc/designs/kporg/kp-foundation/clientlib-structural/assets/images/KPLogoIconBlue.svg"/>
          </div>
          <span class="screenreader-only" lang="en-US">
           Kaiser Permanente Home
          </span>
         </a>
         <!-- Mobile Buttons -->
         <button aria-labelledby="navigation-menu-text" class="mobile-menu-button" data-analytics-location="mobile-menu-button">
          <span class="screenreader-only" id="navigation-menu-text">
           Navigation Menu - Opens a Simulated Dialog
          </span>
          <i class="icon-menu">
          </i>
         </button>
         <!-- Mobile(end)-->
         <ul class="top-header_util-links" data-analytics-location="utility-links">
          <li class="-language" data-language="es-US" id="es-US">
           <span>
            <a aria-label="Español, opens a dialog" class="kp-global-language-selector" data-analytics-click="Español" data-analytics-type="hyperlink" data-language-modal="true" href="https://espanol.kaiserpermanente.org/es/northern-california/doctors-locations" id="kp-global-language-header-selector-id">
             Español
            </a>
           </span>
          </li>
          <li class="region-selector" id="kp_region_selector-util">
           <nav class="region-select-dropdown " data-analytics-location="region-picker">
            <div aria-hidden="true" class="dropdown-overlay ">
             <span aria-hidden="true" class="select-value" id="region-selected-label">
              N. California
             </span>
             <i aria-hidden="true" class="icon-chevron-down">
             </i>
            </div>
            <select aria-label="Choose Your Region. Use ALT + DOWN ARROW to open the menu." class="select-menu form" id="region-global-select-dropdown" role="listbox">
             <option data-region="" data-region-id="" id="N. California">
              Choose your region
             </option>
             <option class="-options" data-region="California - Northern " data-region-id="MRN" data-region-uri="/northern-california/doctors-locations" id="MRN" value="N. California">
              California - Northern
             </option>
             <option class="-options" data-region="California - Southern" data-region-id="SCA" data-region-uri="/southern-california/doctors-locations" id="SCA" value="S. California">
              California - Southern
             </option>
             <option class="-options" data-region="Colorado - Denver / Boulder / Northern / Mountain areas" data-region-id="DB" data-region-uri="/colorado-denver-boulder-mountain-northern/doctors-locations" id="DB" value="Colorado - D/B/N/M">
              Colorado - Denver / Boulder / Northern / Mountain areas
             </option>
             <option class="-options" data-region="Colorado - Southern " data-region-id="CS" data-region-uri="/southern-colorado/doctors-locations" id="CS" value="S. Colorado">
              Colorado - Southern
             </option>
             <option class="-options" data-region="Georgia" data-region-id="GGA" data-region-uri="/georgia/doctors-locations" id="GGA" value="Georgia">
              Georgia
             </option>
             <option class="-options" data-region="Hawaii" data-region-id="HAW" data-region-uri="/hawaii/doctors-locations" id="HAW" value="Hawaii">
              Hawaii
             </option>
             <option class="-options" data-region="Maryland / Virginia / Washington, D.C." data-region-id="MID" data-region-uri="/maryland-virginia-washington-dc/doctors-locations" id="MID" value="Md. / Va. / D.C.">
              Maryland / Virginia / Washington, D.C.
             </option>
             <option class="-options" data-region="Oregon / Washington" data-region-id="KNW" data-region-uri="/oregon-washington/doctors-locations" id="KNW" value="Ore. / Wash.">
              Oregon / Washington
             </option>
            </select>
           </nav>
          </li>
          <li>
           <a data-analytics-click="Sign on to access care" data-analytics-type="hyperlink" href="/northern-california/sign-on">
            Sign on to access care
           </a>
          </li>
         </ul>
         <span class="menu-title-mobile" id="menu_title_mobile">
          Find Doctors and Locations
         </span>
         <!-- <div class="sign-in" id="sign_in">	
    		<sly  data-sly-use.signOn = "org.kp.foundation.core.use.SignOnUse">	
    			<a href="" class="desktop-link">Sign in to access care</a>		
    		</sly>
    </div> -->
         <div class="top-header-secondary-links" data-analytics-location="secondary-links">
          <ul class="account-user" data-analytics-location="top-header-links" id="top-header-links">
           <li class="language-selector" id="other_languages-topnav">
            <i class="icon-globe">
            </i>
            <a href="https://kp.org/languages">
             Other Languages
            </a>
           </li>
           <li>
            <div class="account-selector-dropdown" id="select-dropdown-account-selector-topnav" role="application">
             <div id="account-details-dropdown">
              <a aria-haspopup="true" class="select-value" href="javascript:void(0)" id="acct_user_name-topnav">
               <i aria-hidden="true" class="icon-zz004-profile-border">
               </i>
              </a>
              <i aria-hidden="true" class="icon-chevron-down">
              </i>
             </div>
             <ul data-analytics-location="account-details-topnav" id="account-details-select-dropdown-id-topnav" role="menu">
              <li>
               <a aria-posinset="1" aria-setsize="3" class="account-link" data-account-uri="/health/mycare/consumer/myprofilehome/myprofile" href="/health/mycare/consumer/myprofilehome/myprofile" id="account_details_select_option-topnav" role="menuitem">
                Profile and Preferences
               </a>
              </li>
              <li>
               <span data-language="es-US">
                <a aria-posinset="2" aria-setsize="3" class="account-link kp-global-language-selector" data-language-modal="true" href="https://espanol.kaiserpermanente.org/es/northern-california/doctors-locations" id="kp-global-language-header-selector-id-topnav" role="menuitem">
                 Español
                </a>
               </span>
              </li>
              <li id="account-signout-item">
               <a aria-posinset="3" aria-setsize="3" class="account-link" data-account-uri="/health/mycare/logout.wpp" href="/health/mycare/logout.wpp" id="sign_out_link-topnav" role="menuitem">
                Sign out
               </a>
              </li>
             </ul>
            </div>
           </li>
          </ul>
         </div>
        </div>
        <div class="kp-global-menu " id="kp_global_menu" role="region">
         <div class="global-menu-inner ">
          <button aria-labelledby="navigation-menu-close-text-close" class="mobile-menu-button-close">
           <span class="screenreader-only" id="navigation-menu-close-text-close">
            Button close - press enter or select to close menu
           </span>
           <i class="icon-close">
           </i>
          </button>
          <div class="navigation-container" role="navigation">
           <span id="logged_out_topnav">
            <ul class="primary-links-list">
             <li class="menu-item">
              <a href="/northern-california/why-kp">
               Why KP
              </a>
             </li>
             <li class="menu-item">
              <a href="/northern-california/shop-plans">
               Shop Plans
              </a>
             </li>
             <li class="menu-item">
              <a href="/health/care/consumer/locate-our-services/doctors-and-locations">
               Doctors &amp; Locations
              </a>
             </li>
             <li class="menu-item">
              <a href="/northern-california/health-wellness">
               Health &amp; Wellness
              </a>
             </li>
            </ul>
           </span>
           <span id="logged_in_topnav">
            <ul class="primary-links-list">
             <li class="menu-item first-link" hideintopnav="true">
              <a href="/secure/my-health">
               My Health
              </a>
             </li>
             <li class="menu-item " hideintopnav="true">
              <a href="https://healthy.kaiserpermanente.org/health/mycare/consumer/my-health-manager/my-medical-record">
               Medical Record
              </a>
             </li>
             <li class="menu-item " hideintopnav="true">
              <a href="https://healthy.kaiserpermanente.org/health/mycare/consumer/my-health-manager/message-center/">
               Message Center
              </a>
             </li>
             <li class="menu-item " hideintopnav="true">
              <a href="/northern-california/secure/appointments">
               Appointments
              </a>
             </li>
             <li class="menu-item " hideintopnav="true">
              <a href="https://healthy.kaiserpermanente.org/health/mycare/consumer/pharmacy/">
               Pharmacy
              </a>
             </li>
             <li class="menu-item " hideintopnav="true">
              <a href="https://healthy.kaiserpermanente.org/health/mycare/consumer/my-health-manager/my-plan-and-coverage">
               Coverage &amp; Costs
              </a>
             </li>
             <li class="menu-item " hideintopnav="true">
              <a href="/northern-california/health-wellness">
               Health &amp; Wellness
              </a>
             </li>
             <li class="menu-item menu-item-hide " hideintopnav="true">
              <a href="/northern-california/secure/new-members/get-started">
               Get started
              </a>
             </li>
            </ul>
           </span>
           <a class="mobile-sign-in-button mobile-link" data-analytics-click="Sign in to access care" data-analytics-type="hyperlink" href="/health/care/signon">
            Sign in to access care
           </a>
           <div class="secondary-list-search-container">
            <ul class="secondary-links-list">
             <div class="account-user" data-analytics-location="account-detail" id="acct_user">
              <div>
               <li class="language-selector" id="other_languages_topnav">
                <i class="icon-globe">
                </i>
                <a class="account-link" data-analytics-click="Other Languages" data-analytics-type="hyperlink" href="https://kp.org/languages">
                 Other Languages
                </a>
               </li>
               <li>
                <div class="account-selector-dropdown" id="select-dropdown-account-selector-topnav">
                 <ul aria-labelledby="account_details-topnav" aria-role="menu" data-analytics-location="account-details-topnav" id="account-details-select-dropdown-id-topnav">
                  <li>
                   <a class="account-link" data-account-uri="/health/mycare/consumer/myprofilehome/myprofile" href="/health/mycare/consumer/myprofilehome/myprofile" id="account_details_select_option-topnav">
                    Profile and Preferences
                   </a>
                  </li>
                  <li>
                   <span data-language="es-US">
                    <a class="account-link kp-global-language-selector" data-analytics-click="language picker: Español" data-analytics-type="hyperlink" data-language-modal="true" href="https://espanol.kaiserpermanente.org/es/northern-california/doctors-locations" id="kp-global-language-header-selector-id-topnav">
                     Español
                    </a>
                   </span>
                  </li>
                  <li id="account-signout-item">
                   <a class="account-link" data-account-uri="/health/mycare/logout.wpp" href="/health/mycare/logout.wpp" id="sign_out_link-topnav">
                    Sign out
                   </a>
                  </li>
                 </ul>
                 <span data-account="accountdetails" id="account_details-topnav">
                  end of list
                 </span>
                </div>
               </li>
              </div>
             </div>
             <li class="language-selector" data-analytics-location="language picker: top nav" id="kp_current_language">
              <ul class="-options">
               <li class="-language" data-language="es-US" id="es-US">
                <span>
                 <a aria-label="Español, opens a dialog" class="kp-global-language-selector" data-language-modal="true" href="https://espanol.kaiserpermanente.org/es/northern-california/doctors-locations" id="kp-global-language-header-selector-id">
                  Español
                 </a>
                </span>
               </li>
               <li class="language-selector" id="other_languages" name="language-selector">
                <i class="icon-globe">
                </i>
                <a href="https://kp.org/languages">
                 Other Languages
                </a>
               </li>
              </ul>
             </li>
             <li class="region-selector--main-nav" id="kp_region_selector">
              <nav class="region-select-dropdown" data-analytics-location="region-picker-mobile">
               <div aria-hidden="true" class="dropdown-overlay">
                <span aria-hidden="true" class="select-value" id="region-selected-label">
                 N. California
                </span>
                <i aria-hidden="true" class="icon-chevron-down">
                </i>
               </div>
               <select aria-label="N. California" class="form" id="region-global-select-dropdown-mobile">
                <option data-region="" data-region-id="" id="N. California-mobile">
                 Choose your region
                </option>
                <option class="-options" data-region="California - Northern " data-region-id="MRN" data-region-uri="/northern-california/doctors-locations" id="MRN-mobile" value="N. California">
                 California - Northern
                </option>
                <option class="-options" data-region="California - Southern" data-region-id="SCA" data-region-uri="/southern-california/doctors-locations" id="SCA-mobile" value="S. California">
                 California - Southern
                </option>
                <option class="-options" data-region="Colorado - Denver / Boulder / Northern / Mountain areas" data-region-id="DB" data-region-uri="/colorado-denver-boulder-mountain-northern/doctors-locations" id="DB-mobile" value="Colorado - D/B/N/M">
                 Colorado - Denver / Boulder / Northern / Mountain areas
                </option>
                <option class="-options" data-region="Colorado - Southern " data-region-id="CS" data-region-uri="/southern-colorado/doctors-locations" id="CS-mobile" value="S. Colorado">
                 Colorado - Southern
                </option>
                <option class="-options" data-region="Georgia" data-region-id="GGA" data-region-uri="/georgia/doctors-locations" id="GGA-mobile" value="Georgia">
                 Georgia
                </option>
                <option class="-options" data-region="Hawaii" data-region-id="HAW" data-region-uri="/hawaii/doctors-locations" id="HAW-mobile" value="Hawaii">
                 Hawaii
                </option>
                <option class="-options" data-region="Maryland / Virginia / Washington, D.C." data-region-id="MID" data-region-uri="/maryland-virginia-washington-dc/doctors-locations" id="MID-mobile" value="Md. / Va. / D.C.">
                 Maryland / Virginia / Washington, D.C.
                </option>
                <option class="-options" data-region="Oregon / Washington" data-region-id="KNW" data-region-uri="/oregon-washington/doctors-locations" id="KNW-mobile" value="Ore. / Wash.">
                 Oregon / Washington
                </option>
               </select>
              </nav>
             </li>
            </ul>
            <div class="site-search-container-cl" id="site-search-container">
             <div class="search-bar-parent">
              <div class="search-bar-wrapper bar-collapsed" id="search-bar-wrapper">
               <button aria-labelledby="search-btn-text-id" class="search-bar-icon icon-search" data-track-category="Search Global Header" data-track-link="Search Start" id="site-search-button">
                <span class="search-btn-text " id="search-btn-text-id">
                 Search
                </span>
               </button>
               <div class="category-selector site-search-hidden" id="category-selector">
                <div class="category-search select-dropdown dropdown-notFocus" id="search">
                 <div aria-hidden="true" class="category-search-dropdown dropdown-overlay">
                  <span class="select-value" id="site-search-catigory-selected">
                   All
                  </span>
                  <i class="icon-chevron-down">
                  </i>
                 </div>
                 <select aria-labelledby="search" class="category-search-dropdown-select" id="site-search-category-select">
                  <option label="All" selected="selected" value="All">
                   All
                  </option>
                  <option label="Doctors" value="Doctors">
                   Doctors
                  </option>
                  <option label="Facilities" value="Facilities">
                   Facilities
                  </option>
                  <option label="Classes" value="Classes">
                   Classes
                  </option>
                  <option label="Health Topics" value="Health Topics">
                   Health Topics
                  </option>
                  <option label="Drugs" value="Drug Information">
                   Drugs
                  </option>
                 </select>
                </div>
               </div>
               <!-- end ngIf: searchBar.isOpen -->
               <form class="search-form site-search-hidden" id="site-search-form" name="searchForm">
                <label class="screenreader-only" for="kp-site-search-input">
                 Enter search terms
                </label>
                <input aria-required="true" id="kp-site-search-input" maxlength="50" name="query" placeholder="Start your search" title="Start your search" type="text"/>
                <button aria-hidden="false" class="search-button" disabled="disabled" id="kp-site-search-button" type="button">
                 Search
                </button>
               </form>
               <button aria-label="Close search bar" class="search-bar-icon icon-close close-search-button site-search-hidden" id="site-search-close-button">
                <span class="screenreader-only">
                 Close search bar
                </span>
               </button>
              </div>
             </div>
             <div class="results-page search-modal site-search-hidden" id="search-modal">
              <div class="quick-links-wrapper ">
               <div class="feed-item ">
                <div class="-gutter ">
                 <div class="icon-stethoscope quick-links-care-icon ">
                 </div>
                </div>
                <div class="-main ">
                 <a class="item-heading " href="/health/poc?uri=center:how-to-get-care&amp;nodeid=WPP::M1DJF6EWM">
                  How to get care
                 </a>
                 <div class="-body ">
                  Find urgent care services in your area, including advice and appointment information.
                 </div>
                </div>
               </div>
               <!-- feed item-->
               <div class="feed-item ">
                <div class="-gutter ">
                 <div class="icon-medical-record quick-links-medical-icon ">
                 </div>
                </div>
                <div class="-main ">
                 <a class="item-heading " href="/health/mycare/consumer/my-health-manager/my-medical-record">
                  My Medical Record
                 </a>
                 <div class="-body ">
                  View and print details of your or your family member's medical record, including past visit and hospital stay information, test results, immunizations, health care reminders, and more.
                 </div>
                </div>
               </div>
               <!-- feed item -->
               <div class="feed-item ">
                <div class="-gutter ">
                 <div class="icon-dollar quick-links-pay-icon ">
                 </div>
                </div>
                <div class="-main ">
                 <a class="item-heading " href="/health/poc?uri=center:member-assistance-faq&amp;article=AA8F0E24-5EFE-11E4-A86E-AD44BF9CCEA6">
                  Bill Pay
                 </a>
                 <div class="-body ">
                  Get contact information and find out how to pay premiums, medical bills, and hospital bills online.
                 </div>
                </div>
               </div>
              </div>
             </div>
            </div>
           </div>
          </div>
         </div>
        </div>
       </header>
      </div>
      <div class="kp-body-component" data-analytics-location="kp-body-component" data-region-content="maui">
       <div class="header">
        <div class="container doctors-locations-header" id="container">
         <div>
          <h1 class="regionH1 searchHeader">
           Find doctors and locations
          </h1>
         </div>
         <div>
          <div>
           <p>
            We know how important it is to find a doctor who's right for you. To choose or change doctors at any time, for any reason, browse our online profiles here by region, or call
            <a href="/health/care/consumer/locate-our-services/member-services/hours-and-phone-numbers" target="_self" title="Member services">
             Member services
            </a>
            in your area.
           </p>
          </div>
         </div>
         <div class="searchContent">
          <div>
           <p>
            <b>
             Important:
            </b>
            If you think you're having a
            <a target="_self" title="medical or psychiatric emergency">
             medical or psychiatric emergency
            </a>
            , call 911 or go to the nearest hospital. Do not attempt to access emergency care through this website.
           </p>
          </div>
         </div>
        </div>
       </div>
       <div class="search-app">
        <script>
         window.aemAuthoredData = {"chooseDoctorLabel":"Choose a doctor now","kpLocationsLabel":"KP locations","errorQuerySearch":"Use letters, numbers, and the following symbols only: ' & * - , / .","planTypeLabel":"Plan type","selectDoctorTitle":"Choose your doctor","phoneLabel":"Phone numbers","doctorsLabel":"doctors","errorHelpDesk":"Please come back later and try again.","keywordLabel":"Hospitals, specialties, doctors' names, or keywords","directionsLabel":"Directions","regionLabel":"Region","systemError":"<p><span> We're sorry, but this feature is not available right now.</span><br>\r\n<br>\r\n<span>Please come back later and try again.</span></p>\r\n","emergencyCareLabel":"Emergency care","hospitalLabel":"Hospital name","cityDrOp":"Select city","availableServicesLabel":"Available services","searchTypeLabel":"Search type","spellCheckLabel":"Did you mean","selectDoctorText":"<p>Having a personal doctor who you connect with is an important part of taking care of your health.</p>\r\n","keywordTest":"Enter search terms","filtersLabel":"FILTERS","errorOutage":"Search isn't available right now. Try again later.","orLabel":"OR","errorDefaultText":"Search configuration is incomplete. Please contact the admin.","servicesLabel":"Services at a glance","island":"Island","urgentCareLabel":"Urgent care","cityLabel":"City","fromYourLocation":"from your location","affBhNo":"English: Affiliate / NCA / BH / No / Not Accepting patients messag","affObNo":"English: Affiliate / NCA / OB / No / Not Accepting patients messag","milesFrom":"From","providerTypeDrOp1":"Select provider type","providerTypeLabel":"Provider type","searchNearCurrentLocation":"Searching near your current location","cq:lastRolledout":"java.util.GregorianCalendar[time=1484694039791,areFieldsSet=true,areAllFieldsSet=true,lenient=false,zone=sun.util.calendar.ZoneInfo[id=\"GMT-08:00\",offset=-28800000,dstSavings=0,useDaylight=false,transitions=0,lastRule=null],firstDayOfWeek=1,minimalDaysInFirstWeek=1,ERA=1,YEAR=2017,MONTH=0,WEEK_OF_YEAR=3,WEEK_OF_MONTH=3,DAY_OF_MONTH=17,DAY_OF_YEAR=17,DAY_OF_WEEK=3,DAY_OF_WEEK_IN_MONTH=3,AM_PM=1,HOUR=3,HOUR_OF_DAY=15,MINUTE=0,SECOND=39,MILLISECOND=791,ZONE_OFFSET=-28800000,DST_OFFSET=0]","noEmergencyCareLabel":"No emergency care","myLocationLabel":"My location","filterLabel":"More filters","readLess":"Read less","readMore":"Read more","keyword":"Keyword","zipCodeLabel":"Enter ZIP Code","privacyError":"<p><span>Privacy: We're sorry, but this feature is not available right now.</span><br>\r\n<br>\r\n<span>Please come back later and try again.</span></p>\r\n","fromZip":"from","distanceDrOp1":"Within 5 miles","distanceLabel":"Distance","searchLocal":"Switch to search by city or ZIP code","searchTitle":"What can we help you find?","kpObYes":"Accepting new patients","searchTypeFacilities":"Locations","zipDigits":"5 digits only","languageLabel":"Language","providerType":"Provider Type","unAvailableServicesLabel":"Unavailable services","selectedFiltersLabel":"Selected Filters","resultsInLabel":"in","errorNoResults":"No results for the following search criteria","lessFiltersLabel":"Less filters","noUrgentCareLabel":"No urgent care","currentLocation":"Near your current location","costsVaryLabel":"*costs may vary","newSearchLabel":"New search","city":"City ","mile":"Mile","resultsForLabel":"for","miles":"Miles","viewFacility":"View this facility","heathPlan":"Health Plan","specificLocationLabel":"Specific location","errorEmptySearch":"Please choose at least one search option and try again.","affiliatePhoneLabel":"Information","departmentLabel":"Department","kpPcpYes":"Accepting new patients","afltFacilityHospital":"Kaiser Permanente Affiliate","islandDrOp1":"Select island","islandLabel":"Island","mapHeader":"Select a location below for more information","doctorResultsTitle":"Doctor search results","locationsLabel":"locations","noPharmacyLabel":"No pharmacy","searchButtonLabel":"Search","affPcpYes":"Accepting new patients","searchTypeDoctors":"Doctors","genderLabel":"Gender","useMyLocation":"Use my location","acceptingNewPatientsLabel":"Accepting New Patients?","withinMiles":"WITHIN {{0}} MILES","locationResultsTitle":"Location search results","switchDoctorsText":"Search doctors","afterHoursLabel":"After hours","affiliateLocationsLabel":"Affiliate locations*","plansLabel":"Plans accepted","milesLabel":"Distance","services":"Services","errorZip":"Enter a valid U.S. ZIP code.","switchLocationsText":"Search locations","errorTechFailure":"We're sorry, but this feature is not available right now.","hoursLabel":"Hours","textIsRich":"[Ljava.lang.String;@4ad442ff","chooseDoctorLink":"https://mydoctor.kaiserpermanente.org/cyd?refUrl=https://members.kaiserpermanente.org/kpweb/medicalstaffdir/entrypage.do","errorSorry":"Search isn't available right now. Try again later.","kpFacilityHospital":"Kaiser Permanente Plan Hospital","searchLocalHi":"Switch to search by city, ZIP code, or island","cq:lastRolledoutBy":"admin","specialtyLabel":"Specialty","moreFiltersLabel":"More filters","infoNotAvailable":"This information is not available at this time.","pharmacyLabel":"Pharmacy","hospitalAffiliationLabel":"Hospital name ","milesFromYourLocation":"from your location","resultsFoundLabel":"found","noTitle":"NO TITLE","noAfterHoursLabel":"No after hours","skipMap":"Skip map","regions":[]};
      	window.fdlRwd = "false";
        </script>
        <app-root>
         <!-- Inlined styles ONLY for spinner.. will be removed once angular is bootstrapped -->
         <style>
          .loading-container{position:fixed;z-index:999;overflow:show;margin:auto;top:0;left:0;bottom:0;right:0}.loading-container>div.icon-loading{position:absolute;top:50%;left:50%;transform:translate(-50%,-50%)}.loading-container>div.icon-loading:before{background-size:4em;height:4em;width:4em}.loading-container:before{content:'';display:block;position:fixed;top:0;left:0;width:100%;height:100%;background-color:rgba(255,255,255,0.5)}
         </style>
         <div class="loading-container">
          <div aria-busy="true" aria-label="page loading indicator is visible" aria-live="assertive" class="icon-loading" role="alertdialog">
           <span>
           </span>
          </div>
         </div>
        </app-root>
       </div>
       <div class="footer">
        <hr class="hrLine"/>
        <div class="container doctors-locations-footer" id="container">
         <div class="column-3 marginRemove">
          <h4 class="footer-heading-title desktop">
           Find Out About
          </h4>
          <a aria-expanded="false" class="footer-heading-title mobile" href="javascript:void(0);">
           Find Out About
          </a>
          <ul class="open-list">
           <li>
            <a href="/health/poc?uri=content:ancillary&amp;ctype=help&amp;tid=WPP::LAWR8Y8RR&amp;tname=site_context&amp;rtype=rop" lang="en-US">
             Help with finding doctors and locations
            </a>
           </li>
           <li>
            <a href="/health/poc?uri=content:ancillary&amp;ctype=informational&amp;tid=WPP::LAWRKYLZT&amp;tname=site_context&amp;rtype=rop" lang="en-US">
             Our physicians
            </a>
           </li>
           <li>
            <a class="external-link" href="https://kpdoc.org/cydKPorgref" lang="en-US">
             Choosing your doctor
             <span class="screenreader-only">
              External Link
             </span>
             <i aria-hidden="true" class="icon-link-out extlink">
             </i>
            </a>
           </li>
           <li>
            <a href="/health/poc?uri=content:ancillary&amp;ctype=informational&amp;tid=WPP::LAWRJFNJW&amp;tname=site_context&amp;rtype=rop" lang="en-US">
             Affiliated providers
            </a>
           </li>
           <li>
            <a href="/health/poc?uri=content:ancillary&amp;ctype=informational&amp;tid=WPP::OMV1YSA4U&amp;tname=site_context&amp;rtype=rop" lang="en-US">
             Durable medical equipment
            </a>
           </li>
           <li>
            <a href="/health/poc?uri=content:ancillary&amp;ctype=informational&amp;tid=WPP::OMV1XY2GD&amp;tname=site_context&amp;rtype=rop" lang="en-US">
             Breastfeeding counseling and resources
            </a>
           </li>
           <li>
            <a class="external-link" href="https://kpdoc.org/travelKPorgref" lang="en-US">
             International travel services
             <span class="screenreader-only">
              External Link
             </span>
             <i aria-hidden="true" class="icon-link-out extlink">
             </i>
            </a>
           </li>
           <li>
            <a href="/health/poc?uri=content:ancillary&amp;ctype=glossary&amp;tname=site_context&amp;tid=WPP::LAWRA0N6U&amp;rtype=rop" lang="en-US">
             Glossary
            </a>
           </li>
           <li>
            <a href="/health/care/consumer/center/!ut/p/a1/hY7Ra8IwGMT_Fh_6GL4v1mSJb42z0patirK5vIyshFqoSShB2X-_ruKjeHBwB8fxAw1H0M5cutbEzjvT_3fNv_NyXytFM6xZzbB4YxtZ8vc5rl7gE0rQbe9_pvHXKcawTDDBawiNd9G62Iy2Q4KgzRC7prdwFIoLmS9WRAgqCaVrSiRbUJIzmSohePaq5NO3W3LmPB6e_JVET1obSWMGO1LpCRzTYjeBb7YcsRDVofqQVYo4vw8eKEMIZ_Gb9pewzmazPwf9OWU!/dl5/d5/L2dBISEvZ0FBIS9nQSEh/" lang="en-US">
             Timely access to care
            </a>
           </li>
          </ul>
         </div>
         <div class="column-3 marginRemove">
          <h4 class="footer-heading-title desktop">
           Related Links
          </h4>
          <a aria-expanded="false" class="footer-heading-title mobile" href="javascript:void(0);">
           Related Links
          </a>
          <ul class="open-list">
           <li>
            <a href="/health/poc?uri=content:ancillary&amp;ctype=risk_mitigation&amp;tid=WPP::L6P61N672&amp;tname=site_context&amp;rtype=rop" lang="en-US">
             What is emergency and urgent care?
            </a>
           </li>
           <li>
            <a href="/health/mycare/consumer/locate-our-services/member-services/contact-member-services" lang="en-US">
             Contact Member Services
            </a>
           </li>
           <li>
            <a href="/health/poc?uri=center:how-to-get-care&amp;article=DE975D32-4514-11E0-BB14-ACCAE9FA5AAA" lang="en-US">
             How to get care
            </a>
           </li>
           <li>
            <a href="/health/poc?uri=center:quality-safety" lang="en-US">
             Quality and safety at KP
            </a>
           </li>
           <li>
            <a class="external-link" href="http://www.deltadentalins.com/find-a-dentist?d_loc=&amp;d_kw=&amp;d_d=15&amp;d_net=30&amp;d_prg=delta&amp;d_co=delta" lang="en-US">
             DeltaCare USA network for Eligible Pediatric Enrollees
             <span class="screenreader-only">
              External Link
             </span>
             <i aria-hidden="true" class="icon-link-out extlink">
             </i>
            </a>
           </li>
          </ul>
         </div>
         <div class="column-6 imp-note">
          <h3 id="expandCollapseTitle">
           Your personal doctor
          </h3>
          <div class="fullText" style="display:none">
           <span>
            <p>
             An important part of your health care is building a personal relationship with your doctor.
            </p>
            <p>
             To select a primary care physician,
             <a>
             </a>
             <a target="_self" title="search our doctors ">
             </a>
             <a href="https://mydoctor.kaiserpermanente.org/ncal/mdo/#/" title="search our doctors">
              search our doctors
             </a>
             or
             <a target="_self" title="call us">
             </a>
             <a href="/health/care/consumer/locate-our-services/member-services/hours-and-phone-numbers" title="call us">
              call us
             </a>
             and we'll help find an available doctor near you.
            </p>
            <p>
             To make an appointment or get advice, call 866-454-8855.
             <br/>
            </p>
           </span>
          </div>
          <div class="shortText">
          </div>
          <div>
           <a href="#" id="viewmore" style="display:none">
            More
           </a>
          </div>
          <div>
           <a href="#" id="viewless" style="display:none">
            Less
           </a>
          </div>
          <script>
           $( document ).ready(function() {
            var $pTag = $("div.fullText").find('span');
    		var shortText = $pTag.html();
    		if(shortText.length >350){
                 shortText = shortText.substring(0,350);
                 $('#viewmore').show();
                 }
            $("div.shortText").append('<p>'+shortText+'</p>');
    	});
    
        $('#viewmore').click(function(e) {
            $('.shortText').hide();
            $('#viewmore').hide();
            $('#viewless').show();
           	$("div.fullText").show();
            e.preventDefault();
         });
    
         $('#viewless').click(function(e)
          {    
          	$('#viewless').hide();
       		$("div.fullText").hide();
          	$('.shortText').show();
            $('#viewmore').show();
            $('#expandCollapseTitle').attr("tabindex",0).focus();
            e.preventDefault();
         });
          </script>
         </div>
        </div>
        <div class="container doctors-locations-disclaimer" id="container">
         <p>
          <b>
           To find:
          </b>
         </p>
         <ul>
          <li>
           a provider's office hours, search our facility directory
          </li>
          <li>
           providers in your plan or accepting new patients, call 1-800-464-4000 (toll free) or 711 (TTY for the hearing/speech impaired)
          </li>
         </ul>
         <p>
          The information in this online directory is updated periodically. The availability of physicians, hospitals, providers, and services may change. Information about a practitioner is provided to us by the practitioner or is obtained as part of the credentialing process. If you have questions, please call us at 1-800-464-4000 (toll free). For the hearing and speech impaired: 1-800-464-4000 (toll free) or TTY 711 (toll free). You can also call the Medical Board of California at 916-263-2382, or visit
          <a class="external-link" href="http://www.mbc.ca.gov/" target="_blank" title="their website">
           their website
           <span class="screenreader-only">
            External Link
           </span>
           <i aria-hidden="true" class="icon-link-out extlink">
           </i>
          </a>
          .
         </p>
         <p>
          We want to speak to you in the language that you’re most comfortable with when you call or visit us. Qualified interpreter services, including sign language, are available at no cost, 24 hours a day, 7 days a week during all hours of operations at all points of contact. We do not encourage the use of family, friends or minors as interpreters. Only the services of interpreters and qualified staff are used to provide language assistance. These may include bilingual providers, staff, and healthcare interpreters. In-person, telephone, video, and alternative modes of communication are available.
          <a target="_self" title="Learn more about interpreter services">
           Learn more about interpreter services
          </a>
          .
         </p>
         <p>
          If you would like to report an error in provider or facility information,
          <a title="Member Services">
           please contact us
          </a>
          .
         </p>
         <p>
          Kaiser Permanente enrollees have full and equal access to covered services, including enrollees with disabilities as required under the Federal Americans with Disabilities Act of 1990 and Section 504 of the Rehabilitation Act of 1973.
         </p>
         <p>
          Kaiser Permanente uses the same quality, member experience, or cost-related measures to select practitioners and facilities in Marketplace Silver-tier plans as it does for all other Kaiser Foundation Health Plan (KFHP) products and lines of business. Members enrolled in KFHP Marketplace plans have access to all professional, institutional and ancillary health care providers who participate in KFHP plans’ contracted provider network, in accordance with the terms of members’ KFHP plan of coverage. All Kaiser Permanente Medical Group physicians and network physicians are subject to the same quality review processes and certifications.
         </p>
         <p>
          Kaiser Permanente uses the same geographic distribution consideration to select hospitals in Marketplace plans as it does for all other Kaiser Foundation Health Plan (KFHP) products and lines of business. Accessibility of medical offices and medical centers in this directory: All Kaiser Permanente facilities are accessible to members.
         </p>
        </div>
       </div>
      </div>
      <div id="kp-hoverboard">
      </div>
      <footer class="kp-global-footer-component">
       <div class="kp-footer" data-analytics-location="kp-footer">
        <div class="nav upper four-columns">
         <!-- Footer Navigation Links -->
         <section class="accordion-container">
          <div class="content">
           <h4 class="footer-heading-title desktop">
            Find Care
           </h4>
           <a aria-controls="get_care" aria-expanded="false" class="footer-heading-title mobile" href="javascript:void(0);">
            Find Care
           </a>
           <ul class="open-list" id="get_care">
            <li>
             <a href="/doctors-locations/how-to-find-care/get-advice" lang="en-US">
              Advice
             </a>
            </li>
            <li>
             <a href="/doctors-locations/how-to-find-care/routine-care" lang="en-US">
              Routine Care
             </a>
            </li>
            <li>
             <a href="/doctors-locations/how-to-find-care/urgent-care" lang="en-US">
              Urgent Care
             </a>
            </li>
            <li>
             <a href="/doctors-locations/how-to-find-care/emergency-care" lang="en-US">
              Emergency Care
             </a>
            </li>
            <li>
             <a href="/health/care/consumer/locate-our-services/doctors-and-locations" lang="en-US">
              Find Doctors &amp; Locations
             </a>
            </li>
            <li>
             <a href="/doctors-locations/how-to-find-care/behavioral-health" lang="en-US">
              Behavioral Health
             </a>
            </li>
            <li>
             <a href="/health/care/consumer/health-wellness/programs-classes" lang="en-US">
              Health Classes
             </a>
            </li>
            <li>
             <a href="/health/poc?uri=center:travel-health" lang="en-US">
              When Traveling
             </a>
            </li>
            <li>
             <a href="/health/poc?uri=center:how-to-get-care&amp;article=8B689F4C-8819-11E1-9541-F593B886ADB9" lang="en-US">
              Timely Access to Care
             </a>
            </li>
           </ul>
          </div>
         </section>
         <section class="accordion-container">
          <div class="content">
           <h4 class="footer-heading-title desktop">
            Our Organization
           </h4>
           <a aria-controls="our_org" aria-expanded="false" class="footer-heading-title mobile" href="javascript:void(0);">
            Our Organization
           </a>
           <ul class="open-list" id="our_org">
            <li>
             <a href="/health/poc?uri=center:about-kp">
              About KP
             </a>
            </li>
            <li>
             <a href="http://share.kaiserpermanente.org">
              News &amp; Views
             </a>
            </li>
            <li>
             <a href="http://share.kaiserpermanente.org/category/about-community-benefit">
              Commitment to the Community
             </a>
            </li>
            <li>
             <a href="/health/poc?uri=content:ancillary&amp;ctype=informational&amp;tname=site_context&amp;tid=WPP::LOYOSY40I">
              Diversity &amp; Inclusion
             </a>
            </li>
            <li>
             <a href="/health/poc?uri=content:ancillary&amp;ctype=informational&amp;tid=WPP::LJIAW0MN4&amp;tname=site_context">
              Awards &amp; Accreditations
             </a>
            </li>
            <li>
             <a href="https://kp.org/annualreport">
              Annual Report
             </a>
            </li>
            <li>
             <a href="https://kp.org/careers">
              Careers
             </a>
            </li>
            <li>
             <a href="http://share.kaiserpermanente.org/contact-us/media-contacts/">
              Media Inquiries
             </a>
            </li>
           </ul>
          </div>
         </section>
         <section class="accordion-container">
          <div class="content">
           <h4 class="footer-heading-title desktop">
            Member Support
           </h4>
           <a aria-controls="member_support" aria-expanded="false" class="footer-heading-title mobile" href="javascript:void(0);">
            Member Support
           </a>
           <ul class="open-list" id="member_support">
            <li>
             <a href="/new-members/">
              New Member Welcome
             </a>
            </li>
            <li>
             <a href="/health/poc?uri=center:forms-and-publications">
              Forms &amp; Publications
             </a>
            </li>
            <li>
             <a href="/health/care/consumer/member-assistance">
              Member Assistance
             </a>
            </li>
            <li>
             <a href="/health/care/consumer/locate-our-services/member-services/">
              Member Services
             </a>
            </li>
            <li>
             <a href="/health/poc?uri=center:information-requests&amp;nodeid=WPP::NI51IUJQ2" lang="en-US">
              Medical information requests
             </a>
            </li>
           </ul>
          </div>
         </section>
         <section class="accordion-container">
          <div class="content">
           <h4 class="footer-heading-title desktop">
            Visit Our Other Sites
           </h4>
           <a aria-controls="visit_other" aria-expanded="false" class="footer-heading-title mobile" href="javascript:void(0);">
            Visit Our Other Sites
           </a>
           <ul class="open-list" id="visit_other">
            <li>
             <a href="https://individual-family.kaiserpermanente.org/healthinsurance">
              Individual &amp; Family Plans
             </a>
            </li>
            <li>
             <a href="https://thrive.kaiserpermanente.org/medicaid">
              Medicaid/Medi-Cal
             </a>
            </li>
            <li>
             <a href="https://medicare.kaiserpermanente.org">
              Medicare
             </a>
            </li>
            <li>
             <a href="http://healthreform.kaiserpermanente.org/">
              Affordable Care Act
             </a>
            </li>
            <li>
             <a href="https://businesshealth.kaiserpermanente.org">
              For Businesses
             </a>
            </li>
            <li>
             <a href="https://account.kp.org/broker-employer/resources/broker">
              Broker Support
             </a>
            </li>
           </ul>
          </div>
          <div class="content language-container" id="language-selector">
           <h4 class="language-heading">
            Language
           </h4>
           <ul class="open-list" id="fourth-column">
            <li>
             <a data-language="es" data-language-modal="true" data-language-uri="https://espanol.kaiserpermanente.org/es/northern-california/doctors-locations" href="https://espanol.kaiserpermanente.org/es/northern-california/doctors-locations">
              Español
             </a>
            </li>
            <li>
             <i aria-label="Globe Icon" class="icon-globe" role="img">
             </i>
             <a class="other-language" href="https://kp.org/languages">
              Other Languages
             </a>
            </li>
           </ul>
          </div>
         </section>
        </div>
        <!-- Secondary Footer Menu Links -->
        <div class="lower">
         <div>
          <div class="social-header section">
           <h2 class="follow-text">
            Follow Us
           </h2>
          </div>
          <div class="social-links section" role="navigation">
           <ul class="social-icon-list horizontal-list">
            <li>
             <a class="icon-twitter" data-skip-ext-icon="true" href="https://twitter.com/kpthrive" lang="en-US" title="twitter">
              <span>
               twitter Icon
              </span>
             </a>
            </li>
            <li>
             <a class="icon-facebook" data-skip-ext-icon="true" href="https://www.facebook.com/kpthrive" lang="en-US" title="facebook">
              <span>
               facebook Icon
              </span>
             </a>
            </li>
            <li>
             <a class="icon-youtube" data-skip-ext-icon="true" href="http://www.youtube.com/user/kaiserpermanenteorg" lang="en-US" title="youtube">
              <span>
               youtube Icon
              </span>
             </a>
            </li>
            <li>
             <a class="icon-pinterest" data-skip-ext-icon="true" href="https://www.pinterest.com/kpthrive" lang="en-US" title="pinterest">
              <span>
               pinterest Icon
              </span>
             </a>
            </li>
            <li>
             <a class="icon-instagram" data-skip-ext-icon="true" href="https://www.instagram.com/kpthrive/" lang="en-US" title="instagram">
              <span>
               instagram Icon
              </span>
             </a>
            </li>
           </ul>
          </div>
         </div>
         <div>
          <ul class="leg-reg-links horizontal-list -divided" id="secondary_footer_links">
           <li>
            <a href="/health/poc?uri=content:ancillary&amp;ctype=informational&amp;tid=WPP::LXJZXQ4NU&amp;tname=site_context">
             Accessibility
            </a>
           </li>
           <li>
            <a href="https://kp.org/notices">
             Nondiscrimination Notice
            </a>
           </li>
           <li>
            <a href="/health/poc?uri=center:privacy-statement">
             Privacy
            </a>
           </li>
           <li>
            <a href="/health/poc?uri=content:ancillary&amp;ctype=terms_conditions&amp;tid=WPP::KZ39WVLZT&amp;tname=site_context">
             Terms &amp; Conditions
            </a>
           </li>
           <li>
            <a href="/health/poc?uri=center:rights-responsibilities">
             Rights &amp; Responsibilities
            </a>
           </li>
           <li>
            <a href="/health/poc?uri=center:site-policies">
             Site Policies
            </a>
           </li>
           <li>
            <a href="/health/poc?uri=content:ancillary&amp;ctype=informational&amp;tid=WPP::MZ1L3A9B0&amp;tname=site_context">
             Disaster Planning
            </a>
           </li>
           <li>
            <a href="/health/poc?uri=center:technical-information">
             Technical Information
            </a>
           </li>
           <li>
            <a href="/health/care/consumer/site-map">
             Site Map
            </a>
           </li>
           <li>
            <a href="/health/care/consumer/locate-our-services/member-services/contact-web-manager">
             Contact Site Manager
            </a>
           </li>
          </ul>
         </div>
         <div class="external-site-link-disclaimer">
          Selecting these links
          <i aria-label="external site icon" class="icon-link-out extlink" role="img">
           <span class="screenreader-only">
            external site icon
           </span>
          </i>
          will take you away from KP.org. Kaiser Permanente is not responsible for the content or policies of external websites.
          <a href="/termsconditions#links" target="_self">
           Details
          </a>
         </div>
         <!-- Footer Copyright -->
         <div class="copyright footer-copy-desktop" x-ms-format-detection="none">
          <p style="line-height: normal;">
          </p>
          <p style="line-height: normal;">
           Kaiser Permanente health plans around the country: Kaiser Foundation Health Plan, Inc., in Northern and Southern California and Hawaii • Kaiser Foundation Health Plan of Colorado • Kaiser Foundation Health Plan of Georgia, Inc., Nine Piedmont Center, 3495 Piedmont Road NE, Atlanta, GA 30305, 404-364-7000 • Kaiser Foundation Health Plan of the Mid-Atlantic States, Inc., in Maryland, Virginia, and Washington, D.C., 2101 E. Jefferson St., Rockville, MD 20852 • Kaiser Foundation Health Plan of the Northwest, 500 NE Multnomah St., Suite 100, Portland, OR 97232 • Kaiser Foundation Health Plan of Washington or Kaiser Foundation Health Plan of Washington Options, Inc., 601 Union St., Suite 3100, Seattle, WA 98101
           <br/>
          </p>
          <p>
           <a class="external-link" href="https://get.adobe.com/reader/" style="background-color: rgb(238,238,238);">
            Adobe Acrobat Reader
            <span class="screenreader-only">
             External Link
            </span>
            <i aria-hidden="true" class="icon-link-out extlink">
            </i>
           </a>
           is required to read PDFs.
           <br/>
          </p>
          <p>
           Copyright © 2018 Kaiser Foundation Health Plan, Inc.
          </p>
         </div>
         <div class="secondary-copyright footer-copy-mobile">
          <p style="line-height: normal;">
           Kaiser Permanente health plans around the country: Kaiser Foundation Health Plan, Inc., in Northern and Southern California and Hawaii • Kaiser Foundation Health Plan of Colorado • Kaiser Foundation Health Plan of Georgia, Inc., Nine Piedmont Center, 3495 Piedmont Road NE, Atlanta, GA 30305, 404-364-7000 • Kaiser Foundation Health Plan of the Mid-Atlantic States, Inc., in Maryland, Virginia, and Washington, D.C., 2101 E. Jefferson St., Rockville, MD 20852 • Kaiser Foundation Health Plan of the Northwest, 500 NE Multnomah St., Suite 100, Portland, OR 97232 • Kaiser Foundation Health Plan of Washington or Kaiser Foundation Health Plan of Washington Options, Inc., 601 Union St., Suite 3100, Seattle, WA 98101
           <br/>
           <br/>
          </p>
          <p>
           Copyright © 2017 Kaiser Foundation Health Plan, Inc.
           <br/>
          </p>
         </div>
         <!-- Footer Trustee -->
         <div class="footer-trust-e">
          <a data-skip-ext-icon="true" href="https://privacy.truste.com/privacy-seal/validation?rid=83bcfa89-f6b6-4931-8826-9c6e86322922" target="_blank">
           <img alt="TRUSTe privacy certification program" src="https://privacy-policy.truste.com/privacy-seal/seal?rid=83bcfa89-f6b6-4931-8826-9c6e86322922"/>
          </a>
         </div>
        </div>
       </div>
      </footer>
      <div class="kp-foundation-modal">
       <div>
        <div aria-describedby="language-modal-description" aria-labelledby="language-modal-title" class="global-language-modal kp-modal" data-language-modal-container="" id="global-language-modal-id" lang="es-US" role="dialog">
         <div class="modal-fade-screen">
          <div class="modal-inner" role="document" tabindex="-1">
           <button class="-close" id="modal-close">
            <span class="screenreader-only">
             close modal
            </span>
           </button>
           <header class="modal-header">
            <h2 id="language-modal-title" tabindex="-1">
             Importante
            </h2>
           </header>
           <div class="modal-content" id="language-modal-description" tabindex="-1">
            <p>
             Usted ha elegido ver nuestro sitio web en español.
            </p>
            <p>
             Estamos trabajando para que más funciones estén disponibles en español. Sin embargo, algunas páginas y funciones solo aparecen en inglés.
            </p>
            <div class="language-modal-checkbox-container">
             <input aria-labelledby="language-checkbox-label" class="form-control" id="language-checkbox-toggle" type="checkbox"/>
             <label for="language-checkbox-toggle" id="language-checkbox-label">
              No volver a mostrar esto.
             </label>
            </div>
           </div>
           <div class="modal-buttons ada-buttons-desktop">
            <button class="button -action" id="language-modal-button-cancel">
             Cancelar
            </button>
            <button class="button -action -inverted" id="language-modal-button-continue">
             Continuar
            </button>
           </div>
           <div class="modal-buttons ada-buttons-mobile">
            <button class="button -action -inverted" id="language-modal-button-continue">
             Continuar
            </button>
            <button class="button -action" id="language-modal-button-cancel">
             Cancelar
            </button>
           </div>
          </div>
         </div>
        </div>
       </div>
       <div>
        <div aria-describedby="region-modal-description" aria-labelledby="region-modal-title" class="global-region-modal kp-modal" data-disable-modal="true" data-region-modal-container="" id="global-region-modal-id" lang="en-US" role="dialog">
         <div class="modal-fade-screen">
          <div class="modal-inner" role="document" tabindex="-1">
           <button class="-close" id="global-region-modal-close">
            <span class="screenreader-only">
             close regional modal
            </span>
           </button>
           <header class="modal-header">
            <h2 id="region-modal-title" tabindex="0">
             Choose your region
            </h2>
           </header>
           <div class="modal-content" id="region-modal-description">
            <p>
             Select your region from the list below.
            </p>
            <nav class="region-select-radio-options" data-analytics-location="region-picker-modal">
             <fieldset>
              <legend>
               Regions
              </legend>
              <input class="radio-button" data-region-id="MRN" id="region-code-MRN" name="region-input-radio-select" type="radio" value="/northern-california/doctors-locations"/>
              <label for="region-code-MRN">
               California - Northern
              </label>
              <br/>
              <input class="radio-button" data-region-id="SCA" id="region-code-SCA" name="region-input-radio-select" type="radio" value="/southern-california/doctors-locations"/>
              <label for="region-code-SCA">
               California - Southern
              </label>
              <br/>
              <input class="radio-button" data-region-id="DB" id="region-code-DB" name="region-input-radio-select" type="radio" value="/colorado-denver-boulder-mountain-northern/doctors-locations"/>
              <label for="region-code-DB">
               Colorado - Denver / Boulder / Northern / Mountain areas
              </label>
              <br/>
              <input class="radio-button" data-region-id="CS" id="region-code-CS" name="region-input-radio-select" type="radio" value="/southern-colorado/doctors-locations"/>
              <label for="region-code-CS">
               Colorado - Southern
              </label>
              <br/>
              <input class="radio-button" data-region-id="GGA" id="region-code-GGA" name="region-input-radio-select" type="radio" value="/georgia/doctors-locations"/>
              <label for="region-code-GGA">
               Georgia
              </label>
              <br/>
              <input class="radio-button" data-region-id="HAW" id="region-code-HAW" name="region-input-radio-select" type="radio" value="/hawaii/doctors-locations"/>
              <label for="region-code-HAW">
               Hawaii
              </label>
              <br/>
              <input class="radio-button" data-region-id="MID" id="region-code-MID" name="region-input-radio-select" type="radio" value="/maryland-virginia-washington-dc/doctors-locations"/>
              <label for="region-code-MID">
               Maryland / Virginia / Washington, D.C.
              </label>
              <br/>
              <input class="radio-button" data-region-id="KNW" id="region-code-KNW" name="region-input-radio-select" type="radio" value="/oregon-washington/doctors-locations"/>
              <label for="region-code-KNW">
               Oregon / Washington
              </label>
              <br/>
             </fieldset>
            </nav>
           </div>
           <div class="modal-buttons ada-buttons-desktop">
            <button class="button -action" id="region-modal-button-cancel">
             Cancel
            </button>
            <button class="button -disabled" disabled="true" id="region-modal-button-continue">
             Continue
            </button>
           </div>
           <div class="modal-buttons ada-buttons-mobile">
            <button class="button -disabled" disabled="true" id="region-modal-button-continue">
             Continue
            </button>
            <button class="button -action" id="region-modal-button-cancel">
             Cancel
            </button>
           </div>
          </div>
         </div>
        </div>
       </div>
      </div>
      <script type="text/javascript">
       if(_satellite){
    _satellite.pageBottom();
    }
      </script>
      <script src="/etc/designs/kporg/doctors-locations/clientlib.22b86e252b70e948454dc9fc6163a959.js" type="text/javascript">
      </script>
      <div class="cloudservice testandtarget">
       <script type="text/javascript">
        CQ_Analytics.TestTarget.maxProfileParams = 11;
    
        if (CQ_Analytics.CCM) {
            if (CQ_Analytics.CCM.areStoresInitialized) {
                CQ_Analytics.TestTarget.registerMboxUpdateCalls();
            } else {
                CQ_Analytics.CCM.addListener("storesinitialize", function (e) {
                    CQ_Analytics.TestTarget.registerMboxUpdateCalls();
                });
            }
        } else {
            // client context not there, still register calls
            CQ_Analytics.TestTarget.registerMboxUpdateCalls();
        }
       </script>
      </div>
     </body>
    </html>



```python
# Visit website using Splinter
browser.visit(kaiser_url)

 
```


```python
# Select California - Northern from dropdown menu
browser.select("Region", "NCA")

# Select Redwood City from City dropdown
browser.select("city-dropdown-li", "Redwood City")

 
```


```python
# Select doctors at Kaiser Permanente, Northern California Region within the Redwood City Office 
browser.click_link_by_id('searchButton')
```


```python
# list of physicians dictionary
list_of_physicians = {} 
 
#loop through all the physicians 20 * 3 to get the 60 doctors. 20 from each page.

browser.visit(url)
for x in range(3):

    #loop through all the 20 Physicians from each pagination.
    #results = soup.find_all('div', class_='tab content')
    results = soup.find_all("div")
    print(results)

    Practicing_Address = []
    for r in results:
        el = r.find_all("div", class_="result-list")
        each_dr = el.find("div", class_="detail-data") #each dr info

        # Create BeautifulSoup object; parse with 'html.parser'
        html = browser.html
        soup = BeautifulSoup(html, 'html.parser')

        Physician Name = soup.find("a", class_="bold-font doctorTitle").get_text()

        Physician Specialty = soup.find("div", class_="specialtyMarginlineSpacing").strip()

        medical_location = soup.find("span")[0].text
        street_address = soup.find("span")[1].text
        city = soup.find("span")[2].text
        state = soup.find("span")[3].text
        zipcode = soup.find("span")[4].text

        # Keep a dictionary for each hemisphere. The dictionary contains the title and the feature image.
        Practicing_Adress.append({"medical_location": medical_location, 
                                  "street_address": street_address,
                                  "city": city,
                                  "state": state,
                                  "zipcode": zipcode})

        Phone = soup.find("div", class_"doctorPhone")[none].text()
        

# Add  all the data collected to list_of_physicians dictionary
list_of_physicians["Physician Name"] = Physician Name
list_of_physicians["Physician Specialty"] = Physician Specialty
list_of_physicians["Practicing_Adress"] = Practicing_Adress
list_of_physicians["Phone"] = Phone

```

    [<div aria-describedby="timeout-modal-description" aria-hidden="true" aria-labelledby="timeout-modal-title" class="global-modal-timeout timeout-warning kp-modal" data-element="Modal Appear" data-feature="Find Doctors and Locations" id="global-modal-timeout-id" role="dialog">
    <div class="modal-fade-screen">
    <div class="modal-inner" role="document" tabindex="-1">
    <p><span class="screenreader-only" id="timeout-modal-title">Timeout Warning</span></p>
    <div class="modal-header"><h4 class="page-heading timeout-modal-header">Want to stay signed on?</h4>
      <div> </div>
    </div>
    <div class="content" id="timeout-modal-description">If you haven't used your browser for more than 20 minutes, our system will automatically sign you off to protect your privacy.<br/>
    <br/>
    If you're filling in a form, you'll lose any information you haven't saved when we sign you off.<br/>
    <br/>
    Time remaining before sign off :<span class="countdown-timer"></span>      </div>
    <div class="modal-buttons"><button class="button -action signoff-modal">Sign off</button>            <button class="button -action -inverted ping-alive">Stay signed on</button>               </div>
    </div>
    </div>
    </div>, <div class="modal-fade-screen">
    <div class="modal-inner" role="document" tabindex="-1">
    <p><span class="screenreader-only" id="timeout-modal-title">Timeout Warning</span></p>
    <div class="modal-header"><h4 class="page-heading timeout-modal-header">Want to stay signed on?</h4>
      <div> </div>
    </div>
    <div class="content" id="timeout-modal-description">If you haven't used your browser for more than 20 minutes, our system will automatically sign you off to protect your privacy.<br/>
    <br/>
    If you're filling in a form, you'll lose any information you haven't saved when we sign you off.<br/>
    <br/>
    Time remaining before sign off :<span class="countdown-timer"></span>      </div>
    <div class="modal-buttons"><button class="button -action signoff-modal">Sign off</button>            <button class="button -action -inverted ping-alive">Stay signed on</button>               </div>
    </div>
    </div>, <div class="modal-inner" role="document" tabindex="-1">
    <p><span class="screenreader-only" id="timeout-modal-title">Timeout Warning</span></p>
    <div class="modal-header"><h4 class="page-heading timeout-modal-header">Want to stay signed on?</h4>
      <div> </div>
    </div>
    <div class="content" id="timeout-modal-description">If you haven't used your browser for more than 20 minutes, our system will automatically sign you off to protect your privacy.<br/>
    <br/>
    If you're filling in a form, you'll lose any information you haven't saved when we sign you off.<br/>
    <br/>
    Time remaining before sign off :<span class="countdown-timer"></span>      </div>
    <div class="modal-buttons"><button class="button -action signoff-modal">Sign off</button>            <button class="button -action -inverted ping-alive">Stay signed on</button>               </div>
    </div>, <div class="modal-header"><h4 class="page-heading timeout-modal-header">Want to stay signed on?</h4>
      <div> </div>
    </div>, <div> </div>, <div class="content" id="timeout-modal-description">If you haven't used your browser for more than 20 minutes, our system will automatically sign you off to protect your privacy.<br/>
    <br/>
    If you're filling in a form, you'll lose any information you haven't saved when we sign you off.<br/>
    <br/>
    Time remaining before sign off :<span class="countdown-timer"></span>      </div>, <div class="modal-buttons"><button class="button -action signoff-modal">Sign off</button>            <button class="button -action -inverted ping-alive">Stay signed on</button>               </div>, <div class="kp-global-header-component screen-only" data-analytics-location="kp-global-header">
    <div class="banner">
    <div class="alerts-notification-placeholder" data-uri="/northern-california/alerts/notification.partial.doctors-locations" id="alerts-notification-placeholder-id"></div>
    </div>
    <div data-uri="/northern-california/system/messages/gem/1005.data.json" id="proxy-error-placeholder-id"></div>
    <header class="kp-header blank" data-analytics-location="kp-header" data-header-state="LOGGED_OUT" data-keep-alive="obssobased" id="kp-header">
    <div class="top-header">
    <a class="kp-logo" data-analytics-click="kp-logo" data-analytics-type="image" href="/northern-california" id="accessCare">
    <div class="primary screen-only">
    <img alt="" class="logo-long" src="/etc/designs/kporg/kp-foundation/clientlib-structural/assets/images/logo.svg"/>
    <img alt="" class="logo-short" src="/etc/designs/kporg/kp-foundation/clientlib-structural/assets/images/kp-icon-mini.svg"/>
    <img alt="" class="logo-icon" src="/etc/designs/kporg/kp-foundation/clientlib-structural/assets/images/KPLogoIconBlue.svg"/>
    </div>
    <span class="screenreader-only" lang="en-US">Kaiser Permanente Home</span>
    </a>
    <!-- Mobile Buttons -->
    <button aria-labelledby="navigation-menu-text" class="mobile-menu-button" data-analytics-location="mobile-menu-button">
    <span class="screenreader-only" id="navigation-menu-text">Navigation Menu - Opens a Simulated Dialog</span>
    <i class="icon-menu"></i>
    </button>
    <!-- Mobile(end)-->
    <ul class="top-header_util-links" data-analytics-location="utility-links">
    <li class="-language" data-language="es-US" id="es-US">
    <span>
    <a aria-label="Español, opens a dialog" class="kp-global-language-selector" data-analytics-click="Español" data-analytics-type="hyperlink" data-language-modal="true" href="https://espanol.kaiserpermanente.org/es/northern-california/doctors-locations" id="kp-global-language-header-selector-id">Español</a>
    </span>
    </li>
    <li class="region-selector" id="kp_region_selector-util">
    <nav class="region-select-dropdown " data-analytics-location="region-picker">
    <div aria-hidden="true" class="dropdown-overlay ">
    <span aria-hidden="true" class="select-value" id="region-selected-label">N. California</span>
    <i aria-hidden="true" class="icon-chevron-down"></i>
    </div>
    <select aria-label="Choose Your Region. Use ALT + DOWN ARROW to open the menu." class="select-menu form" id="region-global-select-dropdown" role="listbox">
    <option data-region="" data-region-id="" id="N. California">Choose your region</option>
    <option class="-options" data-region="California - Northern " data-region-id="MRN" data-region-uri="/northern-california/doctors-locations" id="MRN" value="N. California">California - Northern </option><option class="-options" data-region="California - Southern" data-region-id="SCA" data-region-uri="/southern-california/doctors-locations" id="SCA" value="S. California">California - Southern</option><option class="-options" data-region="Colorado - Denver / Boulder / Northern / Mountain areas" data-region-id="DB" data-region-uri="/colorado-denver-boulder-mountain-northern/doctors-locations" id="DB" value="Colorado - D/B/N/M">Colorado - Denver / Boulder / Northern / Mountain areas</option><option class="-options" data-region="Colorado - Southern " data-region-id="CS" data-region-uri="/southern-colorado/doctors-locations" id="CS" value="S. Colorado">Colorado - Southern </option><option class="-options" data-region="Georgia" data-region-id="GGA" data-region-uri="/georgia/doctors-locations" id="GGA" value="Georgia">Georgia</option><option class="-options" data-region="Hawaii" data-region-id="HAW" data-region-uri="/hawaii/doctors-locations" id="HAW" value="Hawaii">Hawaii</option><option class="-options" data-region="Maryland / Virginia / Washington, D.C." data-region-id="MID" data-region-uri="/maryland-virginia-washington-dc/doctors-locations" id="MID" value="Md. / Va. / D.C.">Maryland / Virginia / Washington, D.C.</option><option class="-options" data-region="Oregon / Washington" data-region-id="KNW" data-region-uri="/oregon-washington/doctors-locations" id="KNW" value="Ore. / Wash.">Oregon / Washington</option>
    </select>
    </nav>
    </li>
    <li>
    <a data-analytics-click="Sign on to access care" data-analytics-type="hyperlink" href="/northern-california/sign-on">Sign on to access care</a>
    </li>
    </ul>
    <span class="menu-title-mobile" id="menu_title_mobile">Find Doctors and Locations</span>
    <!-- <div class="sign-in" id="sign_in">	
    		<sly  data-sly-use.signOn = "org.kp.foundation.core.use.SignOnUse">	
    			<a href="" class="desktop-link">Sign in to access care</a>		
    		</sly>
    </div> -->
    <div class="top-header-secondary-links" data-analytics-location="secondary-links">
    <ul class="account-user" data-analytics-location="top-header-links" id="top-header-links">
    <li class="language-selector" id="other_languages-topnav">
    <i class="icon-globe"></i>
    <a href="https://kp.org/languages">Other Languages</a>
    </li>
    <li>
    <div class="account-selector-dropdown" id="select-dropdown-account-selector-topnav" role="application">
    <div id="account-details-dropdown">
    <a aria-haspopup="true" class="select-value" href="javascript:void(0)" id="acct_user_name-topnav"><i aria-hidden="true" class="icon-zz004-profile-border"></i></a>
    <i aria-hidden="true" class="icon-chevron-down"></i>
    </div>
    <ul data-analytics-location="account-details-topnav" id="account-details-select-dropdown-id-topnav" role="menu">
    <li><a aria-posinset="1" aria-setsize="3" class="account-link" data-account-uri="/health/mycare/consumer/myprofilehome/myprofile" href="/health/mycare/consumer/myprofilehome/myprofile" id="account_details_select_option-topnav" role="menuitem">Profile and Preferences</a></li>
    <li>
    <span data-language="es-US">
    <a aria-posinset="2" aria-setsize="3" class="account-link kp-global-language-selector" data-language-modal="true" href="https://espanol.kaiserpermanente.org/es/northern-california/doctors-locations" id="kp-global-language-header-selector-id-topnav" role="menuitem">Español</a>
    </span>
    </li>
    <li id="account-signout-item">
    <a aria-posinset="3" aria-setsize="3" class="account-link" data-account-uri="/health/mycare/logout.wpp" href="/health/mycare/logout.wpp" id="sign_out_link-topnav" role="menuitem">Sign out</a></li>
    </ul>
    </div>
    </li>
    </ul>
    </div>
    </div>
    <div class="kp-global-menu " id="kp_global_menu" role="region">
    <div class="global-menu-inner ">
    <button aria-labelledby="navigation-menu-close-text-close" class="mobile-menu-button-close">
    <span class="screenreader-only" id="navigation-menu-close-text-close">Button close - press enter or select to close menu</span>
    <i class="icon-close"></i>
    </button>
    <div class="navigation-container" role="navigation">
    <span id="logged_out_topnav">
    <ul class="primary-links-list">
    <li class="menu-item"><a href="/northern-california/why-kp">Why KP</a></li>
    <li class="menu-item"><a href="/northern-california/shop-plans">Shop Plans</a></li>
    <li class="menu-item"><a href="/health/care/consumer/locate-our-services/doctors-and-locations">Doctors &amp; Locations</a></li>
    <li class="menu-item"><a href="/northern-california/health-wellness">Health &amp; Wellness</a></li>
    </ul>
    </span>
    <span id="logged_in_topnav">
    <ul class="primary-links-list">
    <li class="menu-item first-link" hideintopnav="true"><a href="/secure/my-health">My Health</a></li>
    <li class="menu-item " hideintopnav="true"><a href="https://healthy.kaiserpermanente.org/health/mycare/consumer/my-health-manager/my-medical-record">Medical Record</a></li>
    <li class="menu-item " hideintopnav="true"><a href="https://healthy.kaiserpermanente.org/health/mycare/consumer/my-health-manager/message-center/">Message Center</a></li>
    <li class="menu-item " hideintopnav="true"><a href="/northern-california/secure/appointments">Appointments</a></li>
    <li class="menu-item " hideintopnav="true"><a href="https://healthy.kaiserpermanente.org/health/mycare/consumer/pharmacy/">Pharmacy</a></li>
    <li class="menu-item " hideintopnav="true"><a href="https://healthy.kaiserpermanente.org/health/mycare/consumer/my-health-manager/my-plan-and-coverage">Coverage &amp; Costs</a></li>
    <li class="menu-item " hideintopnav="true"><a href="/northern-california/health-wellness">Health &amp; Wellness</a></li>
    <li class="menu-item menu-item-hide " hideintopnav="true"><a href="/northern-california/secure/new-members/get-started">Get started</a></li>
    </ul>
    </span>
    <a class="mobile-sign-in-button mobile-link" data-analytics-click="Sign in to access care" data-analytics-type="hyperlink" href="/health/care/signon">Sign in to access care</a>
    <div class="secondary-list-search-container">
    <ul class="secondary-links-list">
    <div class="account-user" data-analytics-location="account-detail" id="acct_user">
    <div>
    <li class="language-selector" id="other_languages_topnav">
    <i class="icon-globe"></i>
    <a class="account-link" data-analytics-click="Other Languages" data-analytics-type="hyperlink" href="https://kp.org/languages">Other Languages</a>
    </li>
    <li>
    <div class="account-selector-dropdown" id="select-dropdown-account-selector-topnav">
    <ul aria-labelledby="account_details-topnav" aria-role="menu" data-analytics-location="account-details-topnav" id="account-details-select-dropdown-id-topnav">
    <li><a class="account-link" data-account-uri="/health/mycare/consumer/myprofilehome/myprofile" href="/health/mycare/consumer/myprofilehome/myprofile" id="account_details_select_option-topnav">Profile and Preferences</a></li>
    <li>
    <span data-language="es-US">
    <a class="account-link kp-global-language-selector" data-analytics-click="language picker: Español" data-analytics-type="hyperlink" data-language-modal="true" href="https://espanol.kaiserpermanente.org/es/northern-california/doctors-locations" id="kp-global-language-header-selector-id-topnav">Español</a>
    </span>
    </li>
    <li id="account-signout-item">
    <a class="account-link" data-account-uri="/health/mycare/logout.wpp" href="/health/mycare/logout.wpp" id="sign_out_link-topnav">Sign out</a></li>
    </ul>
    <span data-account="accountdetails" id="account_details-topnav">end of list</span>
    </div>
    </li>
    </div>
    </div>
    <li class="language-selector" data-analytics-location="language picker: top nav" id="kp_current_language">
    <ul class="-options">
    <li class="-language" data-language="es-US" id="es-US">
    <span>
    <a aria-label="Español, opens a dialog" class="kp-global-language-selector" data-language-modal="true" href="https://espanol.kaiserpermanente.org/es/northern-california/doctors-locations" id="kp-global-language-header-selector-id">Español</a>
    </span>
    </li>
    <li class="language-selector" id="other_languages" name="language-selector"><i class="icon-globe"></i><a href="https://kp.org/languages">Other Languages</a></li>
    </ul>
    </li>
    <li class="region-selector--main-nav" id="kp_region_selector">
    <nav class="region-select-dropdown" data-analytics-location="region-picker-mobile">
    <div aria-hidden="true" class="dropdown-overlay">
    <span aria-hidden="true" class="select-value" id="region-selected-label">N. California</span> <i aria-hidden="true" class="icon-chevron-down"></i>
    </div>
    <select aria-label="N. California" class="form" id="region-global-select-dropdown-mobile">
    <option data-region="" data-region-id="" id="N. California-mobile">Choose your region</option>
    <option class="-options" data-region="California - Northern " data-region-id="MRN" data-region-uri="/northern-california/doctors-locations" id="MRN-mobile" value="N. California">California - Northern </option>
    <option class="-options" data-region="California - Southern" data-region-id="SCA" data-region-uri="/southern-california/doctors-locations" id="SCA-mobile" value="S. California">California - Southern</option>
    <option class="-options" data-region="Colorado - Denver / Boulder / Northern / Mountain areas" data-region-id="DB" data-region-uri="/colorado-denver-boulder-mountain-northern/doctors-locations" id="DB-mobile" value="Colorado - D/B/N/M">Colorado - Denver / Boulder / Northern / Mountain areas</option>
    <option class="-options" data-region="Colorado - Southern " data-region-id="CS" data-region-uri="/southern-colorado/doctors-locations" id="CS-mobile" value="S. Colorado">Colorado - Southern </option>
    <option class="-options" data-region="Georgia" data-region-id="GGA" data-region-uri="/georgia/doctors-locations" id="GGA-mobile" value="Georgia">Georgia</option>
    <option class="-options" data-region="Hawaii" data-region-id="HAW" data-region-uri="/hawaii/doctors-locations" id="HAW-mobile" value="Hawaii">Hawaii</option>
    <option class="-options" data-region="Maryland / Virginia / Washington, D.C." data-region-id="MID" data-region-uri="/maryland-virginia-washington-dc/doctors-locations" id="MID-mobile" value="Md. / Va. / D.C.">Maryland / Virginia / Washington, D.C.</option>
    <option class="-options" data-region="Oregon / Washington" data-region-id="KNW" data-region-uri="/oregon-washington/doctors-locations" id="KNW-mobile" value="Ore. / Wash.">Oregon / Washington</option>
    </select>
    </nav>
    </li>
    </ul>
    <div class="site-search-container-cl" id="site-search-container">
    <div class="search-bar-parent">
    <div class="search-bar-wrapper bar-collapsed" id="search-bar-wrapper">
    <button aria-labelledby="search-btn-text-id" class="search-bar-icon icon-search" data-track-category="Search Global Header" data-track-link="Search Start" id="site-search-button">
    <span class="search-btn-text " id="search-btn-text-id">Search</span>
    </button>
    <div class="category-selector site-search-hidden" id="category-selector">
    <div class="category-search select-dropdown dropdown-notFocus" id="search">
    <div aria-hidden="true" class="category-search-dropdown dropdown-overlay">
    <span class="select-value" id="site-search-catigory-selected">All</span>
    <i class="icon-chevron-down"></i>
    </div>
    <select aria-labelledby="search" class="category-search-dropdown-select" id="site-search-category-select">
    <option label="All" selected="selected" value="All">All</option>
    <option label="Doctors" value="Doctors">Doctors</option>
    <option label="Facilities" value="Facilities">Facilities</option>
    <option label="Classes" value="Classes">Classes</option>
    <option label="Health Topics" value="Health Topics">Health Topics</option>
    <option label="Drugs" value="Drug Information">Drugs</option>
    </select>
    </div>
    </div>
    <!-- end ngIf: searchBar.isOpen -->
    <form class="search-form site-search-hidden" id="site-search-form" name="searchForm">
    <label class="screenreader-only" for="kp-site-search-input">Enter search terms</label>
    <input aria-required="true" id="kp-site-search-input" maxlength="50" name="query" placeholder="Start your search" title="Start your search" type="text"/>
    <button aria-hidden="false" class="search-button" disabled="disabled" id="kp-site-search-button" type="button">
              Search
            </button>
    </form>
    <button aria-label="Close search bar" class="search-bar-icon icon-close close-search-button site-search-hidden" id="site-search-close-button">
    <span class="screenreader-only">Close search bar</span>
    </button>
    </div>
    </div>
    <div class="results-page search-modal site-search-hidden" id="search-modal">
    <div class="quick-links-wrapper ">
    <div class="feed-item ">
    <div class="-gutter ">
    <div class="icon-stethoscope quick-links-care-icon "></div>
    </div>
    <div class="-main ">
    <a class="item-heading " href="/health/poc?uri=center:how-to-get-care&amp;nodeid=WPP::M1DJF6EWM">
                How to get care
              </a>
    <div class="-body ">
                Find urgent care services in your area, including advice and appointment information.
              </div>
    </div>
    </div>
    <!-- feed item-->
    <div class="feed-item ">
    <div class="-gutter ">
    <div class="icon-medical-record quick-links-medical-icon "></div>
    </div>
    <div class="-main ">
    <a class="item-heading " href="/health/mycare/consumer/my-health-manager/my-medical-record">
                My Medical Record
              </a>
    <div class="-body ">
                View and print details of your or your family member's medical record, including past visit and hospital stay information, test results, immunizations, health care reminders, and more.
              </div>
    </div>
    </div>
    <!-- feed item -->
    <div class="feed-item ">
    <div class="-gutter ">
    <div class="icon-dollar quick-links-pay-icon "></div>
    </div>
    <div class="-main ">
    <a class="item-heading " href="/health/poc?uri=center:member-assistance-faq&amp;article=AA8F0E24-5EFE-11E4-A86E-AD44BF9CCEA6">
                Bill Pay</a>
    <div class="-body ">
                Get contact information and find out how to pay premiums, medical bills, and hospital bills online.
              </div>
    </div>
    </div>
    </div>
    </div>
    </div>
    </div>
    </div>
    </div>
    </div>
    </header>
    </div>, <div class="banner">
    <div class="alerts-notification-placeholder" data-uri="/northern-california/alerts/notification.partial.doctors-locations" id="alerts-notification-placeholder-id"></div>
    </div>, <div class="alerts-notification-placeholder" data-uri="/northern-california/alerts/notification.partial.doctors-locations" id="alerts-notification-placeholder-id"></div>, <div data-uri="/northern-california/system/messages/gem/1005.data.json" id="proxy-error-placeholder-id"></div>, <div class="top-header">
    <a class="kp-logo" data-analytics-click="kp-logo" data-analytics-type="image" href="/northern-california" id="accessCare">
    <div class="primary screen-only">
    <img alt="" class="logo-long" src="/etc/designs/kporg/kp-foundation/clientlib-structural/assets/images/logo.svg"/>
    <img alt="" class="logo-short" src="/etc/designs/kporg/kp-foundation/clientlib-structural/assets/images/kp-icon-mini.svg"/>
    <img alt="" class="logo-icon" src="/etc/designs/kporg/kp-foundation/clientlib-structural/assets/images/KPLogoIconBlue.svg"/>
    </div>
    <span class="screenreader-only" lang="en-US">Kaiser Permanente Home</span>
    </a>
    <!-- Mobile Buttons -->
    <button aria-labelledby="navigation-menu-text" class="mobile-menu-button" data-analytics-location="mobile-menu-button">
    <span class="screenreader-only" id="navigation-menu-text">Navigation Menu - Opens a Simulated Dialog</span>
    <i class="icon-menu"></i>
    </button>
    <!-- Mobile(end)-->
    <ul class="top-header_util-links" data-analytics-location="utility-links">
    <li class="-language" data-language="es-US" id="es-US">
    <span>
    <a aria-label="Español, opens a dialog" class="kp-global-language-selector" data-analytics-click="Español" data-analytics-type="hyperlink" data-language-modal="true" href="https://espanol.kaiserpermanente.org/es/northern-california/doctors-locations" id="kp-global-language-header-selector-id">Español</a>
    </span>
    </li>
    <li class="region-selector" id="kp_region_selector-util">
    <nav class="region-select-dropdown " data-analytics-location="region-picker">
    <div aria-hidden="true" class="dropdown-overlay ">
    <span aria-hidden="true" class="select-value" id="region-selected-label">N. California</span>
    <i aria-hidden="true" class="icon-chevron-down"></i>
    </div>
    <select aria-label="Choose Your Region. Use ALT + DOWN ARROW to open the menu." class="select-menu form" id="region-global-select-dropdown" role="listbox">
    <option data-region="" data-region-id="" id="N. California">Choose your region</option>
    <option class="-options" data-region="California - Northern " data-region-id="MRN" data-region-uri="/northern-california/doctors-locations" id="MRN" value="N. California">California - Northern </option><option class="-options" data-region="California - Southern" data-region-id="SCA" data-region-uri="/southern-california/doctors-locations" id="SCA" value="S. California">California - Southern</option><option class="-options" data-region="Colorado - Denver / Boulder / Northern / Mountain areas" data-region-id="DB" data-region-uri="/colorado-denver-boulder-mountain-northern/doctors-locations" id="DB" value="Colorado - D/B/N/M">Colorado - Denver / Boulder / Northern / Mountain areas</option><option class="-options" data-region="Colorado - Southern " data-region-id="CS" data-region-uri="/southern-colorado/doctors-locations" id="CS" value="S. Colorado">Colorado - Southern </option><option class="-options" data-region="Georgia" data-region-id="GGA" data-region-uri="/georgia/doctors-locations" id="GGA" value="Georgia">Georgia</option><option class="-options" data-region="Hawaii" data-region-id="HAW" data-region-uri="/hawaii/doctors-locations" id="HAW" value="Hawaii">Hawaii</option><option class="-options" data-region="Maryland / Virginia / Washington, D.C." data-region-id="MID" data-region-uri="/maryland-virginia-washington-dc/doctors-locations" id="MID" value="Md. / Va. / D.C.">Maryland / Virginia / Washington, D.C.</option><option class="-options" data-region="Oregon / Washington" data-region-id="KNW" data-region-uri="/oregon-washington/doctors-locations" id="KNW" value="Ore. / Wash.">Oregon / Washington</option>
    </select>
    </nav>
    </li>
    <li>
    <a data-analytics-click="Sign on to access care" data-analytics-type="hyperlink" href="/northern-california/sign-on">Sign on to access care</a>
    </li>
    </ul>
    <span class="menu-title-mobile" id="menu_title_mobile">Find Doctors and Locations</span>
    <!-- <div class="sign-in" id="sign_in">	
    		<sly  data-sly-use.signOn = "org.kp.foundation.core.use.SignOnUse">	
    			<a href="" class="desktop-link">Sign in to access care</a>		
    		</sly>
    </div> -->
    <div class="top-header-secondary-links" data-analytics-location="secondary-links">
    <ul class="account-user" data-analytics-location="top-header-links" id="top-header-links">
    <li class="language-selector" id="other_languages-topnav">
    <i class="icon-globe"></i>
    <a href="https://kp.org/languages">Other Languages</a>
    </li>
    <li>
    <div class="account-selector-dropdown" id="select-dropdown-account-selector-topnav" role="application">
    <div id="account-details-dropdown">
    <a aria-haspopup="true" class="select-value" href="javascript:void(0)" id="acct_user_name-topnav"><i aria-hidden="true" class="icon-zz004-profile-border"></i></a>
    <i aria-hidden="true" class="icon-chevron-down"></i>
    </div>
    <ul data-analytics-location="account-details-topnav" id="account-details-select-dropdown-id-topnav" role="menu">
    <li><a aria-posinset="1" aria-setsize="3" class="account-link" data-account-uri="/health/mycare/consumer/myprofilehome/myprofile" href="/health/mycare/consumer/myprofilehome/myprofile" id="account_details_select_option-topnav" role="menuitem">Profile and Preferences</a></li>
    <li>
    <span data-language="es-US">
    <a aria-posinset="2" aria-setsize="3" class="account-link kp-global-language-selector" data-language-modal="true" href="https://espanol.kaiserpermanente.org/es/northern-california/doctors-locations" id="kp-global-language-header-selector-id-topnav" role="menuitem">Español</a>
    </span>
    </li>
    <li id="account-signout-item">
    <a aria-posinset="3" aria-setsize="3" class="account-link" data-account-uri="/health/mycare/logout.wpp" href="/health/mycare/logout.wpp" id="sign_out_link-topnav" role="menuitem">Sign out</a></li>
    </ul>
    </div>
    </li>
    </ul>
    </div>
    </div>, <div class="primary screen-only">
    <img alt="" class="logo-long" src="/etc/designs/kporg/kp-foundation/clientlib-structural/assets/images/logo.svg"/>
    <img alt="" class="logo-short" src="/etc/designs/kporg/kp-foundation/clientlib-structural/assets/images/kp-icon-mini.svg"/>
    <img alt="" class="logo-icon" src="/etc/designs/kporg/kp-foundation/clientlib-structural/assets/images/KPLogoIconBlue.svg"/>
    </div>, <div aria-hidden="true" class="dropdown-overlay ">
    <span aria-hidden="true" class="select-value" id="region-selected-label">N. California</span>
    <i aria-hidden="true" class="icon-chevron-down"></i>
    </div>, <div class="top-header-secondary-links" data-analytics-location="secondary-links">
    <ul class="account-user" data-analytics-location="top-header-links" id="top-header-links">
    <li class="language-selector" id="other_languages-topnav">
    <i class="icon-globe"></i>
    <a href="https://kp.org/languages">Other Languages</a>
    </li>
    <li>
    <div class="account-selector-dropdown" id="select-dropdown-account-selector-topnav" role="application">
    <div id="account-details-dropdown">
    <a aria-haspopup="true" class="select-value" href="javascript:void(0)" id="acct_user_name-topnav"><i aria-hidden="true" class="icon-zz004-profile-border"></i></a>
    <i aria-hidden="true" class="icon-chevron-down"></i>
    </div>
    <ul data-analytics-location="account-details-topnav" id="account-details-select-dropdown-id-topnav" role="menu">
    <li><a aria-posinset="1" aria-setsize="3" class="account-link" data-account-uri="/health/mycare/consumer/myprofilehome/myprofile" href="/health/mycare/consumer/myprofilehome/myprofile" id="account_details_select_option-topnav" role="menuitem">Profile and Preferences</a></li>
    <li>
    <span data-language="es-US">
    <a aria-posinset="2" aria-setsize="3" class="account-link kp-global-language-selector" data-language-modal="true" href="https://espanol.kaiserpermanente.org/es/northern-california/doctors-locations" id="kp-global-language-header-selector-id-topnav" role="menuitem">Español</a>
    </span>
    </li>
    <li id="account-signout-item">
    <a aria-posinset="3" aria-setsize="3" class="account-link" data-account-uri="/health/mycare/logout.wpp" href="/health/mycare/logout.wpp" id="sign_out_link-topnav" role="menuitem">Sign out</a></li>
    </ul>
    </div>
    </li>
    </ul>
    </div>, <div class="account-selector-dropdown" id="select-dropdown-account-selector-topnav" role="application">
    <div id="account-details-dropdown">
    <a aria-haspopup="true" class="select-value" href="javascript:void(0)" id="acct_user_name-topnav"><i aria-hidden="true" class="icon-zz004-profile-border"></i></a>
    <i aria-hidden="true" class="icon-chevron-down"></i>
    </div>
    <ul data-analytics-location="account-details-topnav" id="account-details-select-dropdown-id-topnav" role="menu">
    <li><a aria-posinset="1" aria-setsize="3" class="account-link" data-account-uri="/health/mycare/consumer/myprofilehome/myprofile" href="/health/mycare/consumer/myprofilehome/myprofile" id="account_details_select_option-topnav" role="menuitem">Profile and Preferences</a></li>
    <li>
    <span data-language="es-US">
    <a aria-posinset="2" aria-setsize="3" class="account-link kp-global-language-selector" data-language-modal="true" href="https://espanol.kaiserpermanente.org/es/northern-california/doctors-locations" id="kp-global-language-header-selector-id-topnav" role="menuitem">Español</a>
    </span>
    </li>
    <li id="account-signout-item">
    <a aria-posinset="3" aria-setsize="3" class="account-link" data-account-uri="/health/mycare/logout.wpp" href="/health/mycare/logout.wpp" id="sign_out_link-topnav" role="menuitem">Sign out</a></li>
    </ul>
    </div>, <div id="account-details-dropdown">
    <a aria-haspopup="true" class="select-value" href="javascript:void(0)" id="acct_user_name-topnav"><i aria-hidden="true" class="icon-zz004-profile-border"></i></a>
    <i aria-hidden="true" class="icon-chevron-down"></i>
    </div>, <div class="kp-global-menu " id="kp_global_menu" role="region">
    <div class="global-menu-inner ">
    <button aria-labelledby="navigation-menu-close-text-close" class="mobile-menu-button-close">
    <span class="screenreader-only" id="navigation-menu-close-text-close">Button close - press enter or select to close menu</span>
    <i class="icon-close"></i>
    </button>
    <div class="navigation-container" role="navigation">
    <span id="logged_out_topnav">
    <ul class="primary-links-list">
    <li class="menu-item"><a href="/northern-california/why-kp">Why KP</a></li>
    <li class="menu-item"><a href="/northern-california/shop-plans">Shop Plans</a></li>
    <li class="menu-item"><a href="/health/care/consumer/locate-our-services/doctors-and-locations">Doctors &amp; Locations</a></li>
    <li class="menu-item"><a href="/northern-california/health-wellness">Health &amp; Wellness</a></li>
    </ul>
    </span>
    <span id="logged_in_topnav">
    <ul class="primary-links-list">
    <li class="menu-item first-link" hideintopnav="true"><a href="/secure/my-health">My Health</a></li>
    <li class="menu-item " hideintopnav="true"><a href="https://healthy.kaiserpermanente.org/health/mycare/consumer/my-health-manager/my-medical-record">Medical Record</a></li>
    <li class="menu-item " hideintopnav="true"><a href="https://healthy.kaiserpermanente.org/health/mycare/consumer/my-health-manager/message-center/">Message Center</a></li>
    <li class="menu-item " hideintopnav="true"><a href="/northern-california/secure/appointments">Appointments</a></li>
    <li class="menu-item " hideintopnav="true"><a href="https://healthy.kaiserpermanente.org/health/mycare/consumer/pharmacy/">Pharmacy</a></li>
    <li class="menu-item " hideintopnav="true"><a href="https://healthy.kaiserpermanente.org/health/mycare/consumer/my-health-manager/my-plan-and-coverage">Coverage &amp; Costs</a></li>
    <li class="menu-item " hideintopnav="true"><a href="/northern-california/health-wellness">Health &amp; Wellness</a></li>
    <li class="menu-item menu-item-hide " hideintopnav="true"><a href="/northern-california/secure/new-members/get-started">Get started</a></li>
    </ul>
    </span>
    <a class="mobile-sign-in-button mobile-link" data-analytics-click="Sign in to access care" data-analytics-type="hyperlink" href="/health/care/signon">Sign in to access care</a>
    <div class="secondary-list-search-container">
    <ul class="secondary-links-list">
    <div class="account-user" data-analytics-location="account-detail" id="acct_user">
    <div>
    <li class="language-selector" id="other_languages_topnav">
    <i class="icon-globe"></i>
    <a class="account-link" data-analytics-click="Other Languages" data-analytics-type="hyperlink" href="https://kp.org/languages">Other Languages</a>
    </li>
    <li>
    <div class="account-selector-dropdown" id="select-dropdown-account-selector-topnav">
    <ul aria-labelledby="account_details-topnav" aria-role="menu" data-analytics-location="account-details-topnav" id="account-details-select-dropdown-id-topnav">
    <li><a class="account-link" data-account-uri="/health/mycare/consumer/myprofilehome/myprofile" href="/health/mycare/consumer/myprofilehome/myprofile" id="account_details_select_option-topnav">Profile and Preferences</a></li>
    <li>
    <span data-language="es-US">
    <a class="account-link kp-global-language-selector" data-analytics-click="language picker: Español" data-analytics-type="hyperlink" data-language-modal="true" href="https://espanol.kaiserpermanente.org/es/northern-california/doctors-locations" id="kp-global-language-header-selector-id-topnav">Español</a>
    </span>
    </li>
    <li id="account-signout-item">
    <a class="account-link" data-account-uri="/health/mycare/logout.wpp" href="/health/mycare/logout.wpp" id="sign_out_link-topnav">Sign out</a></li>
    </ul>
    <span data-account="accountdetails" id="account_details-topnav">end of list</span>
    </div>
    </li>
    </div>
    </div>
    <li class="language-selector" data-analytics-location="language picker: top nav" id="kp_current_language">
    <ul class="-options">
    <li class="-language" data-language="es-US" id="es-US">
    <span>
    <a aria-label="Español, opens a dialog" class="kp-global-language-selector" data-language-modal="true" href="https://espanol.kaiserpermanente.org/es/northern-california/doctors-locations" id="kp-global-language-header-selector-id">Español</a>
    </span>
    </li>
    <li class="language-selector" id="other_languages" name="language-selector"><i class="icon-globe"></i><a href="https://kp.org/languages">Other Languages</a></li>
    </ul>
    </li>
    <li class="region-selector--main-nav" id="kp_region_selector">
    <nav class="region-select-dropdown" data-analytics-location="region-picker-mobile">
    <div aria-hidden="true" class="dropdown-overlay">
    <span aria-hidden="true" class="select-value" id="region-selected-label">N. California</span> <i aria-hidden="true" class="icon-chevron-down"></i>
    </div>
    <select aria-label="N. California" class="form" id="region-global-select-dropdown-mobile">
    <option data-region="" data-region-id="" id="N. California-mobile">Choose your region</option>
    <option class="-options" data-region="California - Northern " data-region-id="MRN" data-region-uri="/northern-california/doctors-locations" id="MRN-mobile" value="N. California">California - Northern </option>
    <option class="-options" data-region="California - Southern" data-region-id="SCA" data-region-uri="/southern-california/doctors-locations" id="SCA-mobile" value="S. California">California - Southern</option>
    <option class="-options" data-region="Colorado - Denver / Boulder / Northern / Mountain areas" data-region-id="DB" data-region-uri="/colorado-denver-boulder-mountain-northern/doctors-locations" id="DB-mobile" value="Colorado - D/B/N/M">Colorado - Denver / Boulder / Northern / Mountain areas</option>
    <option class="-options" data-region="Colorado - Southern " data-region-id="CS" data-region-uri="/southern-colorado/doctors-locations" id="CS-mobile" value="S. Colorado">Colorado - Southern </option>
    <option class="-options" data-region="Georgia" data-region-id="GGA" data-region-uri="/georgia/doctors-locations" id="GGA-mobile" value="Georgia">Georgia</option>
    <option class="-options" data-region="Hawaii" data-region-id="HAW" data-region-uri="/hawaii/doctors-locations" id="HAW-mobile" value="Hawaii">Hawaii</option>
    <option class="-options" data-region="Maryland / Virginia / Washington, D.C." data-region-id="MID" data-region-uri="/maryland-virginia-washington-dc/doctors-locations" id="MID-mobile" value="Md. / Va. / D.C.">Maryland / Virginia / Washington, D.C.</option>
    <option class="-options" data-region="Oregon / Washington" data-region-id="KNW" data-region-uri="/oregon-washington/doctors-locations" id="KNW-mobile" value="Ore. / Wash.">Oregon / Washington</option>
    </select>
    </nav>
    </li>
    </ul>
    <div class="site-search-container-cl" id="site-search-container">
    <div class="search-bar-parent">
    <div class="search-bar-wrapper bar-collapsed" id="search-bar-wrapper">
    <button aria-labelledby="search-btn-text-id" class="search-bar-icon icon-search" data-track-category="Search Global Header" data-track-link="Search Start" id="site-search-button">
    <span class="search-btn-text " id="search-btn-text-id">Search</span>
    </button>
    <div class="category-selector site-search-hidden" id="category-selector">
    <div class="category-search select-dropdown dropdown-notFocus" id="search">
    <div aria-hidden="true" class="category-search-dropdown dropdown-overlay">
    <span class="select-value" id="site-search-catigory-selected">All</span>
    <i class="icon-chevron-down"></i>
    </div>
    <select aria-labelledby="search" class="category-search-dropdown-select" id="site-search-category-select">
    <option label="All" selected="selected" value="All">All</option>
    <option label="Doctors" value="Doctors">Doctors</option>
    <option label="Facilities" value="Facilities">Facilities</option>
    <option label="Classes" value="Classes">Classes</option>
    <option label="Health Topics" value="Health Topics">Health Topics</option>
    <option label="Drugs" value="Drug Information">Drugs</option>
    </select>
    </div>
    </div>
    <!-- end ngIf: searchBar.isOpen -->
    <form class="search-form site-search-hidden" id="site-search-form" name="searchForm">
    <label class="screenreader-only" for="kp-site-search-input">Enter search terms</label>
    <input aria-required="true" id="kp-site-search-input" maxlength="50" name="query" placeholder="Start your search" title="Start your search" type="text"/>
    <button aria-hidden="false" class="search-button" disabled="disabled" id="kp-site-search-button" type="button">
              Search
            </button>
    </form>
    <button aria-label="Close search bar" class="search-bar-icon icon-close close-search-button site-search-hidden" id="site-search-close-button">
    <span class="screenreader-only">Close search bar</span>
    </button>
    </div>
    </div>
    <div class="results-page search-modal site-search-hidden" id="search-modal">
    <div class="quick-links-wrapper ">
    <div class="feed-item ">
    <div class="-gutter ">
    <div class="icon-stethoscope quick-links-care-icon "></div>
    </div>
    <div class="-main ">
    <a class="item-heading " href="/health/poc?uri=center:how-to-get-care&amp;nodeid=WPP::M1DJF6EWM">
                How to get care
              </a>
    <div class="-body ">
                Find urgent care services in your area, including advice and appointment information.
              </div>
    </div>
    </div>
    <!-- feed item-->
    <div class="feed-item ">
    <div class="-gutter ">
    <div class="icon-medical-record quick-links-medical-icon "></div>
    </div>
    <div class="-main ">
    <a class="item-heading " href="/health/mycare/consumer/my-health-manager/my-medical-record">
                My Medical Record
              </a>
    <div class="-body ">
                View and print details of your or your family member's medical record, including past visit and hospital stay information, test results, immunizations, health care reminders, and more.
              </div>
    </div>
    </div>
    <!-- feed item -->
    <div class="feed-item ">
    <div class="-gutter ">
    <div class="icon-dollar quick-links-pay-icon "></div>
    </div>
    <div class="-main ">
    <a class="item-heading " href="/health/poc?uri=center:member-assistance-faq&amp;article=AA8F0E24-5EFE-11E4-A86E-AD44BF9CCEA6">
                Bill Pay</a>
    <div class="-body ">
                Get contact information and find out how to pay premiums, medical bills, and hospital bills online.
              </div>
    </div>
    </div>
    </div>
    </div>
    </div>
    </div>
    </div>
    </div>
    </div>, <div class="global-menu-inner ">
    <button aria-labelledby="navigation-menu-close-text-close" class="mobile-menu-button-close">
    <span class="screenreader-only" id="navigation-menu-close-text-close">Button close - press enter or select to close menu</span>
    <i class="icon-close"></i>
    </button>
    <div class="navigation-container" role="navigation">
    <span id="logged_out_topnav">
    <ul class="primary-links-list">
    <li class="menu-item"><a href="/northern-california/why-kp">Why KP</a></li>
    <li class="menu-item"><a href="/northern-california/shop-plans">Shop Plans</a></li>
    <li class="menu-item"><a href="/health/care/consumer/locate-our-services/doctors-and-locations">Doctors &amp; Locations</a></li>
    <li class="menu-item"><a href="/northern-california/health-wellness">Health &amp; Wellness</a></li>
    </ul>
    </span>
    <span id="logged_in_topnav">
    <ul class="primary-links-list">
    <li class="menu-item first-link" hideintopnav="true"><a href="/secure/my-health">My Health</a></li>
    <li class="menu-item " hideintopnav="true"><a href="https://healthy.kaiserpermanente.org/health/mycare/consumer/my-health-manager/my-medical-record">Medical Record</a></li>
    <li class="menu-item " hideintopnav="true"><a href="https://healthy.kaiserpermanente.org/health/mycare/consumer/my-health-manager/message-center/">Message Center</a></li>
    <li class="menu-item " hideintopnav="true"><a href="/northern-california/secure/appointments">Appointments</a></li>
    <li class="menu-item " hideintopnav="true"><a href="https://healthy.kaiserpermanente.org/health/mycare/consumer/pharmacy/">Pharmacy</a></li>
    <li class="menu-item " hideintopnav="true"><a href="https://healthy.kaiserpermanente.org/health/mycare/consumer/my-health-manager/my-plan-and-coverage">Coverage &amp; Costs</a></li>
    <li class="menu-item " hideintopnav="true"><a href="/northern-california/health-wellness">Health &amp; Wellness</a></li>
    <li class="menu-item menu-item-hide " hideintopnav="true"><a href="/northern-california/secure/new-members/get-started">Get started</a></li>
    </ul>
    </span>
    <a class="mobile-sign-in-button mobile-link" data-analytics-click="Sign in to access care" data-analytics-type="hyperlink" href="/health/care/signon">Sign in to access care</a>
    <div class="secondary-list-search-container">
    <ul class="secondary-links-list">
    <div class="account-user" data-analytics-location="account-detail" id="acct_user">
    <div>
    <li class="language-selector" id="other_languages_topnav">
    <i class="icon-globe"></i>
    <a class="account-link" data-analytics-click="Other Languages" data-analytics-type="hyperlink" href="https://kp.org/languages">Other Languages</a>
    </li>
    <li>
    <div class="account-selector-dropdown" id="select-dropdown-account-selector-topnav">
    <ul aria-labelledby="account_details-topnav" aria-role="menu" data-analytics-location="account-details-topnav" id="account-details-select-dropdown-id-topnav">
    <li><a class="account-link" data-account-uri="/health/mycare/consumer/myprofilehome/myprofile" href="/health/mycare/consumer/myprofilehome/myprofile" id="account_details_select_option-topnav">Profile and Preferences</a></li>
    <li>
    <span data-language="es-US">
    <a class="account-link kp-global-language-selector" data-analytics-click="language picker: Español" data-analytics-type="hyperlink" data-language-modal="true" href="https://espanol.kaiserpermanente.org/es/northern-california/doctors-locations" id="kp-global-language-header-selector-id-topnav">Español</a>
    </span>
    </li>
    <li id="account-signout-item">
    <a class="account-link" data-account-uri="/health/mycare/logout.wpp" href="/health/mycare/logout.wpp" id="sign_out_link-topnav">Sign out</a></li>
    </ul>
    <span data-account="accountdetails" id="account_details-topnav">end of list</span>
    </div>
    </li>
    </div>
    </div>
    <li class="language-selector" data-analytics-location="language picker: top nav" id="kp_current_language">
    <ul class="-options">
    <li class="-language" data-language="es-US" id="es-US">
    <span>
    <a aria-label="Español, opens a dialog" class="kp-global-language-selector" data-language-modal="true" href="https://espanol.kaiserpermanente.org/es/northern-california/doctors-locations" id="kp-global-language-header-selector-id">Español</a>
    </span>
    </li>
    <li class="language-selector" id="other_languages" name="language-selector"><i class="icon-globe"></i><a href="https://kp.org/languages">Other Languages</a></li>
    </ul>
    </li>
    <li class="region-selector--main-nav" id="kp_region_selector">
    <nav class="region-select-dropdown" data-analytics-location="region-picker-mobile">
    <div aria-hidden="true" class="dropdown-overlay">
    <span aria-hidden="true" class="select-value" id="region-selected-label">N. California</span> <i aria-hidden="true" class="icon-chevron-down"></i>
    </div>
    <select aria-label="N. California" class="form" id="region-global-select-dropdown-mobile">
    <option data-region="" data-region-id="" id="N. California-mobile">Choose your region</option>
    <option class="-options" data-region="California - Northern " data-region-id="MRN" data-region-uri="/northern-california/doctors-locations" id="MRN-mobile" value="N. California">California - Northern </option>
    <option class="-options" data-region="California - Southern" data-region-id="SCA" data-region-uri="/southern-california/doctors-locations" id="SCA-mobile" value="S. California">California - Southern</option>
    <option class="-options" data-region="Colorado - Denver / Boulder / Northern / Mountain areas" data-region-id="DB" data-region-uri="/colorado-denver-boulder-mountain-northern/doctors-locations" id="DB-mobile" value="Colorado - D/B/N/M">Colorado - Denver / Boulder / Northern / Mountain areas</option>
    <option class="-options" data-region="Colorado - Southern " data-region-id="CS" data-region-uri="/southern-colorado/doctors-locations" id="CS-mobile" value="S. Colorado">Colorado - Southern </option>
    <option class="-options" data-region="Georgia" data-region-id="GGA" data-region-uri="/georgia/doctors-locations" id="GGA-mobile" value="Georgia">Georgia</option>
    <option class="-options" data-region="Hawaii" data-region-id="HAW" data-region-uri="/hawaii/doctors-locations" id="HAW-mobile" value="Hawaii">Hawaii</option>
    <option class="-options" data-region="Maryland / Virginia / Washington, D.C." data-region-id="MID" data-region-uri="/maryland-virginia-washington-dc/doctors-locations" id="MID-mobile" value="Md. / Va. / D.C.">Maryland / Virginia / Washington, D.C.</option>
    <option class="-options" data-region="Oregon / Washington" data-region-id="KNW" data-region-uri="/oregon-washington/doctors-locations" id="KNW-mobile" value="Ore. / Wash.">Oregon / Washington</option>
    </select>
    </nav>
    </li>
    </ul>
    <div class="site-search-container-cl" id="site-search-container">
    <div class="search-bar-parent">
    <div class="search-bar-wrapper bar-collapsed" id="search-bar-wrapper">
    <button aria-labelledby="search-btn-text-id" class="search-bar-icon icon-search" data-track-category="Search Global Header" data-track-link="Search Start" id="site-search-button">
    <span class="search-btn-text " id="search-btn-text-id">Search</span>
    </button>
    <div class="category-selector site-search-hidden" id="category-selector">
    <div class="category-search select-dropdown dropdown-notFocus" id="search">
    <div aria-hidden="true" class="category-search-dropdown dropdown-overlay">
    <span class="select-value" id="site-search-catigory-selected">All</span>
    <i class="icon-chevron-down"></i>
    </div>
    <select aria-labelledby="search" class="category-search-dropdown-select" id="site-search-category-select">
    <option label="All" selected="selected" value="All">All</option>
    <option label="Doctors" value="Doctors">Doctors</option>
    <option label="Facilities" value="Facilities">Facilities</option>
    <option label="Classes" value="Classes">Classes</option>
    <option label="Health Topics" value="Health Topics">Health Topics</option>
    <option label="Drugs" value="Drug Information">Drugs</option>
    </select>
    </div>
    </div>
    <!-- end ngIf: searchBar.isOpen -->
    <form class="search-form site-search-hidden" id="site-search-form" name="searchForm">
    <label class="screenreader-only" for="kp-site-search-input">Enter search terms</label>
    <input aria-required="true" id="kp-site-search-input" maxlength="50" name="query" placeholder="Start your search" title="Start your search" type="text"/>
    <button aria-hidden="false" class="search-button" disabled="disabled" id="kp-site-search-button" type="button">
              Search
            </button>
    </form>
    <button aria-label="Close search bar" class="search-bar-icon icon-close close-search-button site-search-hidden" id="site-search-close-button">
    <span class="screenreader-only">Close search bar</span>
    </button>
    </div>
    </div>
    <div class="results-page search-modal site-search-hidden" id="search-modal">
    <div class="quick-links-wrapper ">
    <div class="feed-item ">
    <div class="-gutter ">
    <div class="icon-stethoscope quick-links-care-icon "></div>
    </div>
    <div class="-main ">
    <a class="item-heading " href="/health/poc?uri=center:how-to-get-care&amp;nodeid=WPP::M1DJF6EWM">
                How to get care
              </a>
    <div class="-body ">
                Find urgent care services in your area, including advice and appointment information.
              </div>
    </div>
    </div>
    <!-- feed item-->
    <div class="feed-item ">
    <div class="-gutter ">
    <div class="icon-medical-record quick-links-medical-icon "></div>
    </div>
    <div class="-main ">
    <a class="item-heading " href="/health/mycare/consumer/my-health-manager/my-medical-record">
                My Medical Record
              </a>
    <div class="-body ">
                View and print details of your or your family member's medical record, including past visit and hospital stay information, test results, immunizations, health care reminders, and more.
              </div>
    </div>
    </div>
    <!-- feed item -->
    <div class="feed-item ">
    <div class="-gutter ">
    <div class="icon-dollar quick-links-pay-icon "></div>
    </div>
    <div class="-main ">
    <a class="item-heading " href="/health/poc?uri=center:member-assistance-faq&amp;article=AA8F0E24-5EFE-11E4-A86E-AD44BF9CCEA6">
                Bill Pay</a>
    <div class="-body ">
                Get contact information and find out how to pay premiums, medical bills, and hospital bills online.
              </div>
    </div>
    </div>
    </div>
    </div>
    </div>
    </div>
    </div>
    </div>, <div class="navigation-container" role="navigation">
    <span id="logged_out_topnav">
    <ul class="primary-links-list">
    <li class="menu-item"><a href="/northern-california/why-kp">Why KP</a></li>
    <li class="menu-item"><a href="/northern-california/shop-plans">Shop Plans</a></li>
    <li class="menu-item"><a href="/health/care/consumer/locate-our-services/doctors-and-locations">Doctors &amp; Locations</a></li>
    <li class="menu-item"><a href="/northern-california/health-wellness">Health &amp; Wellness</a></li>
    </ul>
    </span>
    <span id="logged_in_topnav">
    <ul class="primary-links-list">
    <li class="menu-item first-link" hideintopnav="true"><a href="/secure/my-health">My Health</a></li>
    <li class="menu-item " hideintopnav="true"><a href="https://healthy.kaiserpermanente.org/health/mycare/consumer/my-health-manager/my-medical-record">Medical Record</a></li>
    <li class="menu-item " hideintopnav="true"><a href="https://healthy.kaiserpermanente.org/health/mycare/consumer/my-health-manager/message-center/">Message Center</a></li>
    <li class="menu-item " hideintopnav="true"><a href="/northern-california/secure/appointments">Appointments</a></li>
    <li class="menu-item " hideintopnav="true"><a href="https://healthy.kaiserpermanente.org/health/mycare/consumer/pharmacy/">Pharmacy</a></li>
    <li class="menu-item " hideintopnav="true"><a href="https://healthy.kaiserpermanente.org/health/mycare/consumer/my-health-manager/my-plan-and-coverage">Coverage &amp; Costs</a></li>
    <li class="menu-item " hideintopnav="true"><a href="/northern-california/health-wellness">Health &amp; Wellness</a></li>
    <li class="menu-item menu-item-hide " hideintopnav="true"><a href="/northern-california/secure/new-members/get-started">Get started</a></li>
    </ul>
    </span>
    <a class="mobile-sign-in-button mobile-link" data-analytics-click="Sign in to access care" data-analytics-type="hyperlink" href="/health/care/signon">Sign in to access care</a>
    <div class="secondary-list-search-container">
    <ul class="secondary-links-list">
    <div class="account-user" data-analytics-location="account-detail" id="acct_user">
    <div>
    <li class="language-selector" id="other_languages_topnav">
    <i class="icon-globe"></i>
    <a class="account-link" data-analytics-click="Other Languages" data-analytics-type="hyperlink" href="https://kp.org/languages">Other Languages</a>
    </li>
    <li>
    <div class="account-selector-dropdown" id="select-dropdown-account-selector-topnav">
    <ul aria-labelledby="account_details-topnav" aria-role="menu" data-analytics-location="account-details-topnav" id="account-details-select-dropdown-id-topnav">
    <li><a class="account-link" data-account-uri="/health/mycare/consumer/myprofilehome/myprofile" href="/health/mycare/consumer/myprofilehome/myprofile" id="account_details_select_option-topnav">Profile and Preferences</a></li>
    <li>
    <span data-language="es-US">
    <a class="account-link kp-global-language-selector" data-analytics-click="language picker: Español" data-analytics-type="hyperlink" data-language-modal="true" href="https://espanol.kaiserpermanente.org/es/northern-california/doctors-locations" id="kp-global-language-header-selector-id-topnav">Español</a>
    </span>
    </li>
    <li id="account-signout-item">
    <a class="account-link" data-account-uri="/health/mycare/logout.wpp" href="/health/mycare/logout.wpp" id="sign_out_link-topnav">Sign out</a></li>
    </ul>
    <span data-account="accountdetails" id="account_details-topnav">end of list</span>
    </div>
    </li>
    </div>
    </div>
    <li class="language-selector" data-analytics-location="language picker: top nav" id="kp_current_language">
    <ul class="-options">
    <li class="-language" data-language="es-US" id="es-US">
    <span>
    <a aria-label="Español, opens a dialog" class="kp-global-language-selector" data-language-modal="true" href="https://espanol.kaiserpermanente.org/es/northern-california/doctors-locations" id="kp-global-language-header-selector-id">Español</a>
    </span>
    </li>
    <li class="language-selector" id="other_languages" name="language-selector"><i class="icon-globe"></i><a href="https://kp.org/languages">Other Languages</a></li>
    </ul>
    </li>
    <li class="region-selector--main-nav" id="kp_region_selector">
    <nav class="region-select-dropdown" data-analytics-location="region-picker-mobile">
    <div aria-hidden="true" class="dropdown-overlay">
    <span aria-hidden="true" class="select-value" id="region-selected-label">N. California</span> <i aria-hidden="true" class="icon-chevron-down"></i>
    </div>
    <select aria-label="N. California" class="form" id="region-global-select-dropdown-mobile">
    <option data-region="" data-region-id="" id="N. California-mobile">Choose your region</option>
    <option class="-options" data-region="California - Northern " data-region-id="MRN" data-region-uri="/northern-california/doctors-locations" id="MRN-mobile" value="N. California">California - Northern </option>
    <option class="-options" data-region="California - Southern" data-region-id="SCA" data-region-uri="/southern-california/doctors-locations" id="SCA-mobile" value="S. California">California - Southern</option>
    <option class="-options" data-region="Colorado - Denver / Boulder / Northern / Mountain areas" data-region-id="DB" data-region-uri="/colorado-denver-boulder-mountain-northern/doctors-locations" id="DB-mobile" value="Colorado - D/B/N/M">Colorado - Denver / Boulder / Northern / Mountain areas</option>
    <option class="-options" data-region="Colorado - Southern " data-region-id="CS" data-region-uri="/southern-colorado/doctors-locations" id="CS-mobile" value="S. Colorado">Colorado - Southern </option>
    <option class="-options" data-region="Georgia" data-region-id="GGA" data-region-uri="/georgia/doctors-locations" id="GGA-mobile" value="Georgia">Georgia</option>
    <option class="-options" data-region="Hawaii" data-region-id="HAW" data-region-uri="/hawaii/doctors-locations" id="HAW-mobile" value="Hawaii">Hawaii</option>
    <option class="-options" data-region="Maryland / Virginia / Washington, D.C." data-region-id="MID" data-region-uri="/maryland-virginia-washington-dc/doctors-locations" id="MID-mobile" value="Md. / Va. / D.C.">Maryland / Virginia / Washington, D.C.</option>
    <option class="-options" data-region="Oregon / Washington" data-region-id="KNW" data-region-uri="/oregon-washington/doctors-locations" id="KNW-mobile" value="Ore. / Wash.">Oregon / Washington</option>
    </select>
    </nav>
    </li>
    </ul>
    <div class="site-search-container-cl" id="site-search-container">
    <div class="search-bar-parent">
    <div class="search-bar-wrapper bar-collapsed" id="search-bar-wrapper">
    <button aria-labelledby="search-btn-text-id" class="search-bar-icon icon-search" data-track-category="Search Global Header" data-track-link="Search Start" id="site-search-button">
    <span class="search-btn-text " id="search-btn-text-id">Search</span>
    </button>
    <div class="category-selector site-search-hidden" id="category-selector">
    <div class="category-search select-dropdown dropdown-notFocus" id="search">
    <div aria-hidden="true" class="category-search-dropdown dropdown-overlay">
    <span class="select-value" id="site-search-catigory-selected">All</span>
    <i class="icon-chevron-down"></i>
    </div>
    <select aria-labelledby="search" class="category-search-dropdown-select" id="site-search-category-select">
    <option label="All" selected="selected" value="All">All</option>
    <option label="Doctors" value="Doctors">Doctors</option>
    <option label="Facilities" value="Facilities">Facilities</option>
    <option label="Classes" value="Classes">Classes</option>
    <option label="Health Topics" value="Health Topics">Health Topics</option>
    <option label="Drugs" value="Drug Information">Drugs</option>
    </select>
    </div>
    </div>
    <!-- end ngIf: searchBar.isOpen -->
    <form class="search-form site-search-hidden" id="site-search-form" name="searchForm">
    <label class="screenreader-only" for="kp-site-search-input">Enter search terms</label>
    <input aria-required="true" id="kp-site-search-input" maxlength="50" name="query" placeholder="Start your search" title="Start your search" type="text"/>
    <button aria-hidden="false" class="search-button" disabled="disabled" id="kp-site-search-button" type="button">
              Search
            </button>
    </form>
    <button aria-label="Close search bar" class="search-bar-icon icon-close close-search-button site-search-hidden" id="site-search-close-button">
    <span class="screenreader-only">Close search bar</span>
    </button>
    </div>
    </div>
    <div class="results-page search-modal site-search-hidden" id="search-modal">
    <div class="quick-links-wrapper ">
    <div class="feed-item ">
    <div class="-gutter ">
    <div class="icon-stethoscope quick-links-care-icon "></div>
    </div>
    <div class="-main ">
    <a class="item-heading " href="/health/poc?uri=center:how-to-get-care&amp;nodeid=WPP::M1DJF6EWM">
                How to get care
              </a>
    <div class="-body ">
                Find urgent care services in your area, including advice and appointment information.
              </div>
    </div>
    </div>
    <!-- feed item-->
    <div class="feed-item ">
    <div class="-gutter ">
    <div class="icon-medical-record quick-links-medical-icon "></div>
    </div>
    <div class="-main ">
    <a class="item-heading " href="/health/mycare/consumer/my-health-manager/my-medical-record">
                My Medical Record
              </a>
    <div class="-body ">
                View and print details of your or your family member's medical record, including past visit and hospital stay information, test results, immunizations, health care reminders, and more.
              </div>
    </div>
    </div>
    <!-- feed item -->
    <div class="feed-item ">
    <div class="-gutter ">
    <div class="icon-dollar quick-links-pay-icon "></div>
    </div>
    <div class="-main ">
    <a class="item-heading " href="/health/poc?uri=center:member-assistance-faq&amp;article=AA8F0E24-5EFE-11E4-A86E-AD44BF9CCEA6">
                Bill Pay</a>
    <div class="-body ">
                Get contact information and find out how to pay premiums, medical bills, and hospital bills online.
              </div>
    </div>
    </div>
    </div>
    </div>
    </div>
    </div>
    </div>, <div class="secondary-list-search-container">
    <ul class="secondary-links-list">
    <div class="account-user" data-analytics-location="account-detail" id="acct_user">
    <div>
    <li class="language-selector" id="other_languages_topnav">
    <i class="icon-globe"></i>
    <a class="account-link" data-analytics-click="Other Languages" data-analytics-type="hyperlink" href="https://kp.org/languages">Other Languages</a>
    </li>
    <li>
    <div class="account-selector-dropdown" id="select-dropdown-account-selector-topnav">
    <ul aria-labelledby="account_details-topnav" aria-role="menu" data-analytics-location="account-details-topnav" id="account-details-select-dropdown-id-topnav">
    <li><a class="account-link" data-account-uri="/health/mycare/consumer/myprofilehome/myprofile" href="/health/mycare/consumer/myprofilehome/myprofile" id="account_details_select_option-topnav">Profile and Preferences</a></li>
    <li>
    <span data-language="es-US">
    <a class="account-link kp-global-language-selector" data-analytics-click="language picker: Español" data-analytics-type="hyperlink" data-language-modal="true" href="https://espanol.kaiserpermanente.org/es/northern-california/doctors-locations" id="kp-global-language-header-selector-id-topnav">Español</a>
    </span>
    </li>
    <li id="account-signout-item">
    <a class="account-link" data-account-uri="/health/mycare/logout.wpp" href="/health/mycare/logout.wpp" id="sign_out_link-topnav">Sign out</a></li>
    </ul>
    <span data-account="accountdetails" id="account_details-topnav">end of list</span>
    </div>
    </li>
    </div>
    </div>
    <li class="language-selector" data-analytics-location="language picker: top nav" id="kp_current_language">
    <ul class="-options">
    <li class="-language" data-language="es-US" id="es-US">
    <span>
    <a aria-label="Español, opens a dialog" class="kp-global-language-selector" data-language-modal="true" href="https://espanol.kaiserpermanente.org/es/northern-california/doctors-locations" id="kp-global-language-header-selector-id">Español</a>
    </span>
    </li>
    <li class="language-selector" id="other_languages" name="language-selector"><i class="icon-globe"></i><a href="https://kp.org/languages">Other Languages</a></li>
    </ul>
    </li>
    <li class="region-selector--main-nav" id="kp_region_selector">
    <nav class="region-select-dropdown" data-analytics-location="region-picker-mobile">
    <div aria-hidden="true" class="dropdown-overlay">
    <span aria-hidden="true" class="select-value" id="region-selected-label">N. California</span> <i aria-hidden="true" class="icon-chevron-down"></i>
    </div>
    <select aria-label="N. California" class="form" id="region-global-select-dropdown-mobile">
    <option data-region="" data-region-id="" id="N. California-mobile">Choose your region</option>
    <option class="-options" data-region="California - Northern " data-region-id="MRN" data-region-uri="/northern-california/doctors-locations" id="MRN-mobile" value="N. California">California - Northern </option>
    <option class="-options" data-region="California - Southern" data-region-id="SCA" data-region-uri="/southern-california/doctors-locations" id="SCA-mobile" value="S. California">California - Southern</option>
    <option class="-options" data-region="Colorado - Denver / Boulder / Northern / Mountain areas" data-region-id="DB" data-region-uri="/colorado-denver-boulder-mountain-northern/doctors-locations" id="DB-mobile" value="Colorado - D/B/N/M">Colorado - Denver / Boulder / Northern / Mountain areas</option>
    <option class="-options" data-region="Colorado - Southern " data-region-id="CS" data-region-uri="/southern-colorado/doctors-locations" id="CS-mobile" value="S. Colorado">Colorado - Southern </option>
    <option class="-options" data-region="Georgia" data-region-id="GGA" data-region-uri="/georgia/doctors-locations" id="GGA-mobile" value="Georgia">Georgia</option>
    <option class="-options" data-region="Hawaii" data-region-id="HAW" data-region-uri="/hawaii/doctors-locations" id="HAW-mobile" value="Hawaii">Hawaii</option>
    <option class="-options" data-region="Maryland / Virginia / Washington, D.C." data-region-id="MID" data-region-uri="/maryland-virginia-washington-dc/doctors-locations" id="MID-mobile" value="Md. / Va. / D.C.">Maryland / Virginia / Washington, D.C.</option>
    <option class="-options" data-region="Oregon / Washington" data-region-id="KNW" data-region-uri="/oregon-washington/doctors-locations" id="KNW-mobile" value="Ore. / Wash.">Oregon / Washington</option>
    </select>
    </nav>
    </li>
    </ul>
    <div class="site-search-container-cl" id="site-search-container">
    <div class="search-bar-parent">
    <div class="search-bar-wrapper bar-collapsed" id="search-bar-wrapper">
    <button aria-labelledby="search-btn-text-id" class="search-bar-icon icon-search" data-track-category="Search Global Header" data-track-link="Search Start" id="site-search-button">
    <span class="search-btn-text " id="search-btn-text-id">Search</span>
    </button>
    <div class="category-selector site-search-hidden" id="category-selector">
    <div class="category-search select-dropdown dropdown-notFocus" id="search">
    <div aria-hidden="true" class="category-search-dropdown dropdown-overlay">
    <span class="select-value" id="site-search-catigory-selected">All</span>
    <i class="icon-chevron-down"></i>
    </div>
    <select aria-labelledby="search" class="category-search-dropdown-select" id="site-search-category-select">
    <option label="All" selected="selected" value="All">All</option>
    <option label="Doctors" value="Doctors">Doctors</option>
    <option label="Facilities" value="Facilities">Facilities</option>
    <option label="Classes" value="Classes">Classes</option>
    <option label="Health Topics" value="Health Topics">Health Topics</option>
    <option label="Drugs" value="Drug Information">Drugs</option>
    </select>
    </div>
    </div>
    <!-- end ngIf: searchBar.isOpen -->
    <form class="search-form site-search-hidden" id="site-search-form" name="searchForm">
    <label class="screenreader-only" for="kp-site-search-input">Enter search terms</label>
    <input aria-required="true" id="kp-site-search-input" maxlength="50" name="query" placeholder="Start your search" title="Start your search" type="text"/>
    <button aria-hidden="false" class="search-button" disabled="disabled" id="kp-site-search-button" type="button">
              Search
            </button>
    </form>
    <button aria-label="Close search bar" class="search-bar-icon icon-close close-search-button site-search-hidden" id="site-search-close-button">
    <span class="screenreader-only">Close search bar</span>
    </button>
    </div>
    </div>
    <div class="results-page search-modal site-search-hidden" id="search-modal">
    <div class="quick-links-wrapper ">
    <div class="feed-item ">
    <div class="-gutter ">
    <div class="icon-stethoscope quick-links-care-icon "></div>
    </div>
    <div class="-main ">
    <a class="item-heading " href="/health/poc?uri=center:how-to-get-care&amp;nodeid=WPP::M1DJF6EWM">
                How to get care
              </a>
    <div class="-body ">
                Find urgent care services in your area, including advice and appointment information.
              </div>
    </div>
    </div>
    <!-- feed item-->
    <div class="feed-item ">
    <div class="-gutter ">
    <div class="icon-medical-record quick-links-medical-icon "></div>
    </div>
    <div class="-main ">
    <a class="item-heading " href="/health/mycare/consumer/my-health-manager/my-medical-record">
                My Medical Record
              </a>
    <div class="-body ">
                View and print details of your or your family member's medical record, including past visit and hospital stay information, test results, immunizations, health care reminders, and more.
              </div>
    </div>
    </div>
    <!-- feed item -->
    <div class="feed-item ">
    <div class="-gutter ">
    <div class="icon-dollar quick-links-pay-icon "></div>
    </div>
    <div class="-main ">
    <a class="item-heading " href="/health/poc?uri=center:member-assistance-faq&amp;article=AA8F0E24-5EFE-11E4-A86E-AD44BF9CCEA6">
                Bill Pay</a>
    <div class="-body ">
                Get contact information and find out how to pay premiums, medical bills, and hospital bills online.
              </div>
    </div>
    </div>
    </div>
    </div>
    </div>
    </div>, <div class="account-user" data-analytics-location="account-detail" id="acct_user">
    <div>
    <li class="language-selector" id="other_languages_topnav">
    <i class="icon-globe"></i>
    <a class="account-link" data-analytics-click="Other Languages" data-analytics-type="hyperlink" href="https://kp.org/languages">Other Languages</a>
    </li>
    <li>
    <div class="account-selector-dropdown" id="select-dropdown-account-selector-topnav">
    <ul aria-labelledby="account_details-topnav" aria-role="menu" data-analytics-location="account-details-topnav" id="account-details-select-dropdown-id-topnav">
    <li><a class="account-link" data-account-uri="/health/mycare/consumer/myprofilehome/myprofile" href="/health/mycare/consumer/myprofilehome/myprofile" id="account_details_select_option-topnav">Profile and Preferences</a></li>
    <li>
    <span data-language="es-US">
    <a class="account-link kp-global-language-selector" data-analytics-click="language picker: Español" data-analytics-type="hyperlink" data-language-modal="true" href="https://espanol.kaiserpermanente.org/es/northern-california/doctors-locations" id="kp-global-language-header-selector-id-topnav">Español</a>
    </span>
    </li>
    <li id="account-signout-item">
    <a class="account-link" data-account-uri="/health/mycare/logout.wpp" href="/health/mycare/logout.wpp" id="sign_out_link-topnav">Sign out</a></li>
    </ul>
    <span data-account="accountdetails" id="account_details-topnav">end of list</span>
    </div>
    </li>
    </div>
    </div>, <div>
    <li class="language-selector" id="other_languages_topnav">
    <i class="icon-globe"></i>
    <a class="account-link" data-analytics-click="Other Languages" data-analytics-type="hyperlink" href="https://kp.org/languages">Other Languages</a>
    </li>
    <li>
    <div class="account-selector-dropdown" id="select-dropdown-account-selector-topnav">
    <ul aria-labelledby="account_details-topnav" aria-role="menu" data-analytics-location="account-details-topnav" id="account-details-select-dropdown-id-topnav">
    <li><a class="account-link" data-account-uri="/health/mycare/consumer/myprofilehome/myprofile" href="/health/mycare/consumer/myprofilehome/myprofile" id="account_details_select_option-topnav">Profile and Preferences</a></li>
    <li>
    <span data-language="es-US">
    <a class="account-link kp-global-language-selector" data-analytics-click="language picker: Español" data-analytics-type="hyperlink" data-language-modal="true" href="https://espanol.kaiserpermanente.org/es/northern-california/doctors-locations" id="kp-global-language-header-selector-id-topnav">Español</a>
    </span>
    </li>
    <li id="account-signout-item">
    <a class="account-link" data-account-uri="/health/mycare/logout.wpp" href="/health/mycare/logout.wpp" id="sign_out_link-topnav">Sign out</a></li>
    </ul>
    <span data-account="accountdetails" id="account_details-topnav">end of list</span>
    </div>
    </li>
    </div>, <div class="account-selector-dropdown" id="select-dropdown-account-selector-topnav">
    <ul aria-labelledby="account_details-topnav" aria-role="menu" data-analytics-location="account-details-topnav" id="account-details-select-dropdown-id-topnav">
    <li><a class="account-link" data-account-uri="/health/mycare/consumer/myprofilehome/myprofile" href="/health/mycare/consumer/myprofilehome/myprofile" id="account_details_select_option-topnav">Profile and Preferences</a></li>
    <li>
    <span data-language="es-US">
    <a class="account-link kp-global-language-selector" data-analytics-click="language picker: Español" data-analytics-type="hyperlink" data-language-modal="true" href="https://espanol.kaiserpermanente.org/es/northern-california/doctors-locations" id="kp-global-language-header-selector-id-topnav">Español</a>
    </span>
    </li>
    <li id="account-signout-item">
    <a class="account-link" data-account-uri="/health/mycare/logout.wpp" href="/health/mycare/logout.wpp" id="sign_out_link-topnav">Sign out</a></li>
    </ul>
    <span data-account="accountdetails" id="account_details-topnav">end of list</span>
    </div>, <div aria-hidden="true" class="dropdown-overlay">
    <span aria-hidden="true" class="select-value" id="region-selected-label">N. California</span> <i aria-hidden="true" class="icon-chevron-down"></i>
    </div>, <div class="site-search-container-cl" id="site-search-container">
    <div class="search-bar-parent">
    <div class="search-bar-wrapper bar-collapsed" id="search-bar-wrapper">
    <button aria-labelledby="search-btn-text-id" class="search-bar-icon icon-search" data-track-category="Search Global Header" data-track-link="Search Start" id="site-search-button">
    <span class="search-btn-text " id="search-btn-text-id">Search</span>
    </button>
    <div class="category-selector site-search-hidden" id="category-selector">
    <div class="category-search select-dropdown dropdown-notFocus" id="search">
    <div aria-hidden="true" class="category-search-dropdown dropdown-overlay">
    <span class="select-value" id="site-search-catigory-selected">All</span>
    <i class="icon-chevron-down"></i>
    </div>
    <select aria-labelledby="search" class="category-search-dropdown-select" id="site-search-category-select">
    <option label="All" selected="selected" value="All">All</option>
    <option label="Doctors" value="Doctors">Doctors</option>
    <option label="Facilities" value="Facilities">Facilities</option>
    <option label="Classes" value="Classes">Classes</option>
    <option label="Health Topics" value="Health Topics">Health Topics</option>
    <option label="Drugs" value="Drug Information">Drugs</option>
    </select>
    </div>
    </div>
    <!-- end ngIf: searchBar.isOpen -->
    <form class="search-form site-search-hidden" id="site-search-form" name="searchForm">
    <label class="screenreader-only" for="kp-site-search-input">Enter search terms</label>
    <input aria-required="true" id="kp-site-search-input" maxlength="50" name="query" placeholder="Start your search" title="Start your search" type="text"/>
    <button aria-hidden="false" class="search-button" disabled="disabled" id="kp-site-search-button" type="button">
              Search
            </button>
    </form>
    <button aria-label="Close search bar" class="search-bar-icon icon-close close-search-button site-search-hidden" id="site-search-close-button">
    <span class="screenreader-only">Close search bar</span>
    </button>
    </div>
    </div>
    <div class="results-page search-modal site-search-hidden" id="search-modal">
    <div class="quick-links-wrapper ">
    <div class="feed-item ">
    <div class="-gutter ">
    <div class="icon-stethoscope quick-links-care-icon "></div>
    </div>
    <div class="-main ">
    <a class="item-heading " href="/health/poc?uri=center:how-to-get-care&amp;nodeid=WPP::M1DJF6EWM">
                How to get care
              </a>
    <div class="-body ">
                Find urgent care services in your area, including advice and appointment information.
              </div>
    </div>
    </div>
    <!-- feed item-->
    <div class="feed-item ">
    <div class="-gutter ">
    <div class="icon-medical-record quick-links-medical-icon "></div>
    </div>
    <div class="-main ">
    <a class="item-heading " href="/health/mycare/consumer/my-health-manager/my-medical-record">
                My Medical Record
              </a>
    <div class="-body ">
                View and print details of your or your family member's medical record, including past visit and hospital stay information, test results, immunizations, health care reminders, and more.
              </div>
    </div>
    </div>
    <!-- feed item -->
    <div class="feed-item ">
    <div class="-gutter ">
    <div class="icon-dollar quick-links-pay-icon "></div>
    </div>
    <div class="-main ">
    <a class="item-heading " href="/health/poc?uri=center:member-assistance-faq&amp;article=AA8F0E24-5EFE-11E4-A86E-AD44BF9CCEA6">
                Bill Pay</a>
    <div class="-body ">
                Get contact information and find out how to pay premiums, medical bills, and hospital bills online.
              </div>
    </div>
    </div>
    </div>
    </div>
    </div>, <div class="search-bar-parent">
    <div class="search-bar-wrapper bar-collapsed" id="search-bar-wrapper">
    <button aria-labelledby="search-btn-text-id" class="search-bar-icon icon-search" data-track-category="Search Global Header" data-track-link="Search Start" id="site-search-button">
    <span class="search-btn-text " id="search-btn-text-id">Search</span>
    </button>
    <div class="category-selector site-search-hidden" id="category-selector">
    <div class="category-search select-dropdown dropdown-notFocus" id="search">
    <div aria-hidden="true" class="category-search-dropdown dropdown-overlay">
    <span class="select-value" id="site-search-catigory-selected">All</span>
    <i class="icon-chevron-down"></i>
    </div>
    <select aria-labelledby="search" class="category-search-dropdown-select" id="site-search-category-select">
    <option label="All" selected="selected" value="All">All</option>
    <option label="Doctors" value="Doctors">Doctors</option>
    <option label="Facilities" value="Facilities">Facilities</option>
    <option label="Classes" value="Classes">Classes</option>
    <option label="Health Topics" value="Health Topics">Health Topics</option>
    <option label="Drugs" value="Drug Information">Drugs</option>
    </select>
    </div>
    </div>
    <!-- end ngIf: searchBar.isOpen -->
    <form class="search-form site-search-hidden" id="site-search-form" name="searchForm">
    <label class="screenreader-only" for="kp-site-search-input">Enter search terms</label>
    <input aria-required="true" id="kp-site-search-input" maxlength="50" name="query" placeholder="Start your search" title="Start your search" type="text"/>
    <button aria-hidden="false" class="search-button" disabled="disabled" id="kp-site-search-button" type="button">
              Search
            </button>
    </form>
    <button aria-label="Close search bar" class="search-bar-icon icon-close close-search-button site-search-hidden" id="site-search-close-button">
    <span class="screenreader-only">Close search bar</span>
    </button>
    </div>
    </div>, <div class="search-bar-wrapper bar-collapsed" id="search-bar-wrapper">
    <button aria-labelledby="search-btn-text-id" class="search-bar-icon icon-search" data-track-category="Search Global Header" data-track-link="Search Start" id="site-search-button">
    <span class="search-btn-text " id="search-btn-text-id">Search</span>
    </button>
    <div class="category-selector site-search-hidden" id="category-selector">
    <div class="category-search select-dropdown dropdown-notFocus" id="search">
    <div aria-hidden="true" class="category-search-dropdown dropdown-overlay">
    <span class="select-value" id="site-search-catigory-selected">All</span>
    <i class="icon-chevron-down"></i>
    </div>
    <select aria-labelledby="search" class="category-search-dropdown-select" id="site-search-category-select">
    <option label="All" selected="selected" value="All">All</option>
    <option label="Doctors" value="Doctors">Doctors</option>
    <option label="Facilities" value="Facilities">Facilities</option>
    <option label="Classes" value="Classes">Classes</option>
    <option label="Health Topics" value="Health Topics">Health Topics</option>
    <option label="Drugs" value="Drug Information">Drugs</option>
    </select>
    </div>
    </div>
    <!-- end ngIf: searchBar.isOpen -->
    <form class="search-form site-search-hidden" id="site-search-form" name="searchForm">
    <label class="screenreader-only" for="kp-site-search-input">Enter search terms</label>
    <input aria-required="true" id="kp-site-search-input" maxlength="50" name="query" placeholder="Start your search" title="Start your search" type="text"/>
    <button aria-hidden="false" class="search-button" disabled="disabled" id="kp-site-search-button" type="button">
              Search
            </button>
    </form>
    <button aria-label="Close search bar" class="search-bar-icon icon-close close-search-button site-search-hidden" id="site-search-close-button">
    <span class="screenreader-only">Close search bar</span>
    </button>
    </div>, <div class="category-selector site-search-hidden" id="category-selector">
    <div class="category-search select-dropdown dropdown-notFocus" id="search">
    <div aria-hidden="true" class="category-search-dropdown dropdown-overlay">
    <span class="select-value" id="site-search-catigory-selected">All</span>
    <i class="icon-chevron-down"></i>
    </div>
    <select aria-labelledby="search" class="category-search-dropdown-select" id="site-search-category-select">
    <option label="All" selected="selected" value="All">All</option>
    <option label="Doctors" value="Doctors">Doctors</option>
    <option label="Facilities" value="Facilities">Facilities</option>
    <option label="Classes" value="Classes">Classes</option>
    <option label="Health Topics" value="Health Topics">Health Topics</option>
    <option label="Drugs" value="Drug Information">Drugs</option>
    </select>
    </div>
    </div>, <div class="category-search select-dropdown dropdown-notFocus" id="search">
    <div aria-hidden="true" class="category-search-dropdown dropdown-overlay">
    <span class="select-value" id="site-search-catigory-selected">All</span>
    <i class="icon-chevron-down"></i>
    </div>
    <select aria-labelledby="search" class="category-search-dropdown-select" id="site-search-category-select">
    <option label="All" selected="selected" value="All">All</option>
    <option label="Doctors" value="Doctors">Doctors</option>
    <option label="Facilities" value="Facilities">Facilities</option>
    <option label="Classes" value="Classes">Classes</option>
    <option label="Health Topics" value="Health Topics">Health Topics</option>
    <option label="Drugs" value="Drug Information">Drugs</option>
    </select>
    </div>, <div aria-hidden="true" class="category-search-dropdown dropdown-overlay">
    <span class="select-value" id="site-search-catigory-selected">All</span>
    <i class="icon-chevron-down"></i>
    </div>, <div class="results-page search-modal site-search-hidden" id="search-modal">
    <div class="quick-links-wrapper ">
    <div class="feed-item ">
    <div class="-gutter ">
    <div class="icon-stethoscope quick-links-care-icon "></div>
    </div>
    <div class="-main ">
    <a class="item-heading " href="/health/poc?uri=center:how-to-get-care&amp;nodeid=WPP::M1DJF6EWM">
                How to get care
              </a>
    <div class="-body ">
                Find urgent care services in your area, including advice and appointment information.
              </div>
    </div>
    </div>
    <!-- feed item-->
    <div class="feed-item ">
    <div class="-gutter ">
    <div class="icon-medical-record quick-links-medical-icon "></div>
    </div>
    <div class="-main ">
    <a class="item-heading " href="/health/mycare/consumer/my-health-manager/my-medical-record">
                My Medical Record
              </a>
    <div class="-body ">
                View and print details of your or your family member's medical record, including past visit and hospital stay information, test results, immunizations, health care reminders, and more.
              </div>
    </div>
    </div>
    <!-- feed item -->
    <div class="feed-item ">
    <div class="-gutter ">
    <div class="icon-dollar quick-links-pay-icon "></div>
    </div>
    <div class="-main ">
    <a class="item-heading " href="/health/poc?uri=center:member-assistance-faq&amp;article=AA8F0E24-5EFE-11E4-A86E-AD44BF9CCEA6">
                Bill Pay</a>
    <div class="-body ">
                Get contact information and find out how to pay premiums, medical bills, and hospital bills online.
              </div>
    </div>
    </div>
    </div>
    </div>, <div class="quick-links-wrapper ">
    <div class="feed-item ">
    <div class="-gutter ">
    <div class="icon-stethoscope quick-links-care-icon "></div>
    </div>
    <div class="-main ">
    <a class="item-heading " href="/health/poc?uri=center:how-to-get-care&amp;nodeid=WPP::M1DJF6EWM">
                How to get care
              </a>
    <div class="-body ">
                Find urgent care services in your area, including advice and appointment information.
              </div>
    </div>
    </div>
    <!-- feed item-->
    <div class="feed-item ">
    <div class="-gutter ">
    <div class="icon-medical-record quick-links-medical-icon "></div>
    </div>
    <div class="-main ">
    <a class="item-heading " href="/health/mycare/consumer/my-health-manager/my-medical-record">
                My Medical Record
              </a>
    <div class="-body ">
                View and print details of your or your family member's medical record, including past visit and hospital stay information, test results, immunizations, health care reminders, and more.
              </div>
    </div>
    </div>
    <!-- feed item -->
    <div class="feed-item ">
    <div class="-gutter ">
    <div class="icon-dollar quick-links-pay-icon "></div>
    </div>
    <div class="-main ">
    <a class="item-heading " href="/health/poc?uri=center:member-assistance-faq&amp;article=AA8F0E24-5EFE-11E4-A86E-AD44BF9CCEA6">
                Bill Pay</a>
    <div class="-body ">
                Get contact information and find out how to pay premiums, medical bills, and hospital bills online.
              </div>
    </div>
    </div>
    </div>, <div class="feed-item ">
    <div class="-gutter ">
    <div class="icon-stethoscope quick-links-care-icon "></div>
    </div>
    <div class="-main ">
    <a class="item-heading " href="/health/poc?uri=center:how-to-get-care&amp;nodeid=WPP::M1DJF6EWM">
                How to get care
              </a>
    <div class="-body ">
                Find urgent care services in your area, including advice and appointment information.
              </div>
    </div>
    </div>, <div class="-gutter ">
    <div class="icon-stethoscope quick-links-care-icon "></div>
    </div>, <div class="icon-stethoscope quick-links-care-icon "></div>, <div class="-main ">
    <a class="item-heading " href="/health/poc?uri=center:how-to-get-care&amp;nodeid=WPP::M1DJF6EWM">
                How to get care
              </a>
    <div class="-body ">
                Find urgent care services in your area, including advice and appointment information.
              </div>
    </div>, <div class="-body ">
                Find urgent care services in your area, including advice and appointment information.
              </div>, <div class="feed-item ">
    <div class="-gutter ">
    <div class="icon-medical-record quick-links-medical-icon "></div>
    </div>
    <div class="-main ">
    <a class="item-heading " href="/health/mycare/consumer/my-health-manager/my-medical-record">
                My Medical Record
              </a>
    <div class="-body ">
                View and print details of your or your family member's medical record, including past visit and hospital stay information, test results, immunizations, health care reminders, and more.
              </div>
    </div>
    </div>, <div class="-gutter ">
    <div class="icon-medical-record quick-links-medical-icon "></div>
    </div>, <div class="icon-medical-record quick-links-medical-icon "></div>, <div class="-main ">
    <a class="item-heading " href="/health/mycare/consumer/my-health-manager/my-medical-record">
                My Medical Record
              </a>
    <div class="-body ">
                View and print details of your or your family member's medical record, including past visit and hospital stay information, test results, immunizations, health care reminders, and more.
              </div>
    </div>, <div class="-body ">
                View and print details of your or your family member's medical record, including past visit and hospital stay information, test results, immunizations, health care reminders, and more.
              </div>, <div class="feed-item ">
    <div class="-gutter ">
    <div class="icon-dollar quick-links-pay-icon "></div>
    </div>
    <div class="-main ">
    <a class="item-heading " href="/health/poc?uri=center:member-assistance-faq&amp;article=AA8F0E24-5EFE-11E4-A86E-AD44BF9CCEA6">
                Bill Pay</a>
    <div class="-body ">
                Get contact information and find out how to pay premiums, medical bills, and hospital bills online.
              </div>
    </div>
    </div>, <div class="-gutter ">
    <div class="icon-dollar quick-links-pay-icon "></div>
    </div>, <div class="icon-dollar quick-links-pay-icon "></div>, <div class="-main ">
    <a class="item-heading " href="/health/poc?uri=center:member-assistance-faq&amp;article=AA8F0E24-5EFE-11E4-A86E-AD44BF9CCEA6">
                Bill Pay</a>
    <div class="-body ">
                Get contact information and find out how to pay premiums, medical bills, and hospital bills online.
              </div>
    </div>, <div class="-body ">
                Get contact information and find out how to pay premiums, medical bills, and hospital bills online.
              </div>, <div class="kp-body-component" data-analytics-location="kp-body-component" data-region-content="maui">
    <div class="header"><div class="container doctors-locations-header" id="container">
    <div>
    <h1 class="regionH1 searchHeader">
    
    
    
    Find doctors and locations
    
    </h1>
    </div>
    <div>
    <div> <p>We know how important it is to find a doctor who's right for you. To choose or change doctors at any time, for any reason, browse our online profiles here by region, or call <a href="/health/care/consumer/locate-our-services/member-services/hours-and-phone-numbers" target="_self" title="Member services">Member services</a> in your area.</p>
    </div>
    </div>
    <div class="searchContent">
    <div> <p><b>Important:</b> If you think you're having a <a target="_self" title="medical or psychiatric emergency">medical or psychiatric emergency</a>, call 911 or go to the nearest hospital. Do not attempt to access emergency care through this website.</p>
    </div>
    </div>
    </div></div>
    <div class="search-app">
    <script> 
      	window.aemAuthoredData = {"chooseDoctorLabel":"Choose a doctor now","kpLocationsLabel":"KP locations","errorQuerySearch":"Use letters, numbers, and the following symbols only: ' & * - , / .","planTypeLabel":"Plan type","selectDoctorTitle":"Choose your doctor","phoneLabel":"Phone numbers","doctorsLabel":"doctors","errorHelpDesk":"Please come back later and try again.","keywordLabel":"Hospitals, specialties, doctors' names, or keywords","directionsLabel":"Directions","regionLabel":"Region","systemError":"<p><span> We're sorry, but this feature is not available right now.</span><br>\r\n<br>\r\n<span>Please come back later and try again.</span></p>\r\n","emergencyCareLabel":"Emergency care","hospitalLabel":"Hospital name","cityDrOp":"Select city","availableServicesLabel":"Available services","searchTypeLabel":"Search type","spellCheckLabel":"Did you mean","selectDoctorText":"<p>Having a personal doctor who you connect with is an important part of taking care of your health.</p>\r\n","keywordTest":"Enter search terms","filtersLabel":"FILTERS","errorOutage":"Search isn't available right now. Try again later.","orLabel":"OR","errorDefaultText":"Search configuration is incomplete. Please contact the admin.","servicesLabel":"Services at a glance","island":"Island","urgentCareLabel":"Urgent care","cityLabel":"City","fromYourLocation":"from your location","affBhNo":"English: Affiliate / NCA / BH / No / Not Accepting patients messag","affObNo":"English: Affiliate / NCA / OB / No / Not Accepting patients messag","milesFrom":"From","providerTypeDrOp1":"Select provider type","providerTypeLabel":"Provider type","searchNearCurrentLocation":"Searching near your current location","cq:lastRolledout":"java.util.GregorianCalendar[time=1484694039791,areFieldsSet=true,areAllFieldsSet=true,lenient=false,zone=sun.util.calendar.ZoneInfo[id=\"GMT-08:00\",offset=-28800000,dstSavings=0,useDaylight=false,transitions=0,lastRule=null],firstDayOfWeek=1,minimalDaysInFirstWeek=1,ERA=1,YEAR=2017,MONTH=0,WEEK_OF_YEAR=3,WEEK_OF_MONTH=3,DAY_OF_MONTH=17,DAY_OF_YEAR=17,DAY_OF_WEEK=3,DAY_OF_WEEK_IN_MONTH=3,AM_PM=1,HOUR=3,HOUR_OF_DAY=15,MINUTE=0,SECOND=39,MILLISECOND=791,ZONE_OFFSET=-28800000,DST_OFFSET=0]","noEmergencyCareLabel":"No emergency care","myLocationLabel":"My location","filterLabel":"More filters","readLess":"Read less","readMore":"Read more","keyword":"Keyword","zipCodeLabel":"Enter ZIP Code","privacyError":"<p><span>Privacy: We're sorry, but this feature is not available right now.</span><br>\r\n<br>\r\n<span>Please come back later and try again.</span></p>\r\n","fromZip":"from","distanceDrOp1":"Within 5 miles","distanceLabel":"Distance","searchLocal":"Switch to search by city or ZIP code","searchTitle":"What can we help you find?","kpObYes":"Accepting new patients","searchTypeFacilities":"Locations","zipDigits":"5 digits only","languageLabel":"Language","providerType":"Provider Type","unAvailableServicesLabel":"Unavailable services","selectedFiltersLabel":"Selected Filters","resultsInLabel":"in","errorNoResults":"No results for the following search criteria","lessFiltersLabel":"Less filters","noUrgentCareLabel":"No urgent care","currentLocation":"Near your current location","costsVaryLabel":"*costs may vary","newSearchLabel":"New search","city":"City ","mile":"Mile","resultsForLabel":"for","miles":"Miles","viewFacility":"View this facility","heathPlan":"Health Plan","specificLocationLabel":"Specific location","errorEmptySearch":"Please choose at least one search option and try again.","affiliatePhoneLabel":"Information","departmentLabel":"Department","kpPcpYes":"Accepting new patients","afltFacilityHospital":"Kaiser Permanente Affiliate","islandDrOp1":"Select island","islandLabel":"Island","mapHeader":"Select a location below for more information","doctorResultsTitle":"Doctor search results","locationsLabel":"locations","noPharmacyLabel":"No pharmacy","searchButtonLabel":"Search","affPcpYes":"Accepting new patients","searchTypeDoctors":"Doctors","genderLabel":"Gender","useMyLocation":"Use my location","acceptingNewPatientsLabel":"Accepting New Patients?","withinMiles":"WITHIN {{0}} MILES","locationResultsTitle":"Location search results","switchDoctorsText":"Search doctors","afterHoursLabel":"After hours","affiliateLocationsLabel":"Affiliate locations*","plansLabel":"Plans accepted","milesLabel":"Distance","services":"Services","errorZip":"Enter a valid U.S. ZIP code.","switchLocationsText":"Search locations","errorTechFailure":"We're sorry, but this feature is not available right now.","hoursLabel":"Hours","textIsRich":"[Ljava.lang.String;@4ad442ff","chooseDoctorLink":"https://mydoctor.kaiserpermanente.org/cyd?refUrl=https://members.kaiserpermanente.org/kpweb/medicalstaffdir/entrypage.do","errorSorry":"Search isn't available right now. Try again later.","kpFacilityHospital":"Kaiser Permanente Plan Hospital","searchLocalHi":"Switch to search by city, ZIP code, or island","cq:lastRolledoutBy":"admin","specialtyLabel":"Specialty","moreFiltersLabel":"More filters","infoNotAvailable":"This information is not available at this time.","pharmacyLabel":"Pharmacy","hospitalAffiliationLabel":"Hospital name ","milesFromYourLocation":"from your location","resultsFoundLabel":"found","noTitle":"NO TITLE","noAfterHoursLabel":"No after hours","skipMap":"Skip map","regions":[]};
      	window.fdlRwd = "false";
      </script>
    <app-root>
    <!-- Inlined styles ONLY for spinner.. will be removed once angular is bootstrapped -->
    <style>.loading-container{position:fixed;z-index:999;overflow:show;margin:auto;top:0;left:0;bottom:0;right:0}.loading-container>div.icon-loading{position:absolute;top:50%;left:50%;transform:translate(-50%,-50%)}.loading-container>div.icon-loading:before{background-size:4em;height:4em;width:4em}.loading-container:before{content:'';display:block;position:fixed;top:0;left:0;width:100%;height:100%;background-color:rgba(255,255,255,0.5)}</style>
    <div class="loading-container">
    <div aria-busy="true" aria-label="page loading indicator is visible" aria-live="assertive" class="icon-loading" role="alertdialog">
    <span></span>
    </div>
    </div>
    </app-root>
    </div>
    <div class="footer">
    <hr class="hrLine"/>
    <div class="container doctors-locations-footer" id="container">
    <div class="column-3 marginRemove">
    <h4 class="footer-heading-title desktop">
    	Find Out About
    </h4>
    <a aria-expanded="false" class="footer-heading-title mobile" href="javascript:void(0);">Find Out About</a>
    <ul class="open-list">
    <li>
    <a href="/health/poc?uri=content:ancillary&amp;ctype=help&amp;tid=WPP::LAWR8Y8RR&amp;tname=site_context&amp;rtype=rop" lang="en-US">Help with finding doctors and locations</a>
    </li>
    <li>
    <a href="/health/poc?uri=content:ancillary&amp;ctype=informational&amp;tid=WPP::LAWRKYLZT&amp;tname=site_context&amp;rtype=rop" lang="en-US">Our physicians</a>
    </li>
    <li>
    <a class="external-link" href="https://kpdoc.org/cydKPorgref" lang="en-US">Choosing your doctor<span class="screenreader-only">External Link</span><i aria-hidden="true" class="icon-link-out extlink"></i></a>
    </li>
    <li>
    <a href="/health/poc?uri=content:ancillary&amp;ctype=informational&amp;tid=WPP::LAWRJFNJW&amp;tname=site_context&amp;rtype=rop" lang="en-US">Affiliated providers</a>
    </li>
    <li>
    <a href="/health/poc?uri=content:ancillary&amp;ctype=informational&amp;tid=WPP::OMV1YSA4U&amp;tname=site_context&amp;rtype=rop" lang="en-US">Durable medical equipment</a>
    </li>
    <li>
    <a href="/health/poc?uri=content:ancillary&amp;ctype=informational&amp;tid=WPP::OMV1XY2GD&amp;tname=site_context&amp;rtype=rop" lang="en-US">Breastfeeding counseling and resources</a>
    </li>
    <li>
    <a class="external-link" href="https://kpdoc.org/travelKPorgref" lang="en-US">International travel services <span class="screenreader-only">External Link</span><i aria-hidden="true" class="icon-link-out extlink"></i></a>
    </li>
    <li>
    <a href="/health/poc?uri=content:ancillary&amp;ctype=glossary&amp;tname=site_context&amp;tid=WPP::LAWRA0N6U&amp;rtype=rop" lang="en-US">Glossary</a>
    </li>
    <li>
    <a href="/health/care/consumer/center/!ut/p/a1/hY7Ra8IwGMT_Fh_6GL4v1mSJb42z0patirK5vIyshFqoSShB2X-_ruKjeHBwB8fxAw1H0M5cutbEzjvT_3fNv_NyXytFM6xZzbB4YxtZ8vc5rl7gE0rQbe9_pvHXKcawTDDBawiNd9G62Iy2Q4KgzRC7prdwFIoLmS9WRAgqCaVrSiRbUJIzmSohePaq5NO3W3LmPB6e_JVET1obSWMGO1LpCRzTYjeBb7YcsRDVofqQVYo4vw8eKEMIZ_Gb9pewzmazPwf9OWU!/dl5/d5/L2dBISEvZ0FBIS9nQSEh/" lang="en-US">Timely access to care</a>
    </li>
    </ul>
    </div>
    <div class="column-3 marginRemove">
    <h4 class="footer-heading-title desktop">
    	Related Links
    </h4>
    <a aria-expanded="false" class="footer-heading-title mobile" href="javascript:void(0);">Related Links</a>
    <ul class="open-list">
    <li>
    <a href="/health/poc?uri=content:ancillary&amp;ctype=risk_mitigation&amp;tid=WPP::L6P61N672&amp;tname=site_context&amp;rtype=rop" lang="en-US">What is emergency and urgent care?</a>
    </li>
    <li>
    <a href="/health/mycare/consumer/locate-our-services/member-services/contact-member-services" lang="en-US">Contact Member Services</a>
    </li>
    <li>
    <a href="/health/poc?uri=center:how-to-get-care&amp;article=DE975D32-4514-11E0-BB14-ACCAE9FA5AAA" lang="en-US">How to get care</a>
    </li>
    <li>
    <a href="/health/poc?uri=center:quality-safety" lang="en-US">Quality and safety at KP</a>
    </li>
    <li>
    <a class="external-link" href="http://www.deltadentalins.com/find-a-dentist?d_loc=&amp;d_kw=&amp;d_d=15&amp;d_net=30&amp;d_prg=delta&amp;d_co=delta" lang="en-US">DeltaCare USA network for Eligible Pediatric Enrollees<span class="screenreader-only">External Link</span><i aria-hidden="true" class="icon-link-out extlink"></i></a>
    </li>
    </ul>
    </div>
    <div class="column-6 imp-note">
    <h3 id="expandCollapseTitle"> Your personal doctor </h3>
    <div class="fullText" style="display:none">
    <span>
    <p>An important part of your health care is building a personal relationship with your doctor.</p>
    <p>To select a primary care physician, <a></a><a target="_self" title="search our doctors "></a><a href="https://mydoctor.kaiserpermanente.org/ncal/mdo/#/" title="search our doctors">search our doctors</a> or <a target="_self" title="call us"></a><a href="/health/care/consumer/locate-our-services/member-services/hours-and-phone-numbers" title="call us">call us</a> and we'll help find an available doctor near you.</p>
    <p>To make an appointment or get advice, call 866-454-8855.<br/>
    </p>
    </span>
    </div>
    <div class="shortText"></div>
    <div>
    <a href="#" id="viewmore" style="display:none">More</a>
    </div>
    <div>
    <a href="#" id="viewless" style="display:none">Less</a>
    </div>
    <script>
    	$( document ).ready(function() {
            var $pTag = $("div.fullText").find('span');
    		var shortText = $pTag.html();
    		if(shortText.length >350){
                 shortText = shortText.substring(0,350);
                 $('#viewmore').show();
                 }
            $("div.shortText").append('<p>'+shortText+'</p>');
    	});
    
        $('#viewmore').click(function(e) {
            $('.shortText').hide();
            $('#viewmore').hide();
            $('#viewless').show();
           	$("div.fullText").show();
            e.preventDefault();
         });
    
         $('#viewless').click(function(e)
          {    
          	$('#viewless').hide();
       		$("div.fullText").hide();
          	$('.shortText').show();
            $('#viewmore').show();
            $('#expandCollapseTitle').attr("tabindex",0).focus();
            e.preventDefault();
         });
    </script>
    </div>
    </div>
    <div class="container doctors-locations-disclaimer" id="container">
    <p><b>To find:</b></p>
    <ul>
    <li>a provider's office hours, search our facility directory</li>
    <li>providers in your plan or accepting new patients, call 1-800-464-4000 (toll free) or 711 (TTY for the hearing/speech impaired)</li>
    </ul>
    <p>The information in this online directory is updated periodically. The availability of physicians, hospitals, providers, and services may change. Information about a practitioner is provided to us by the practitioner or is obtained as part of the credentialing process. If you have questions, please call us at 1-800-464-4000 (toll free). For the hearing and speech impaired: 1-800-464-4000 (toll free) or TTY 711 (toll free). You can also call the Medical Board of California at 916-263-2382, or visit <a class="external-link" href="http://www.mbc.ca.gov/" target="_blank" title="their website">their website<span class="screenreader-only">External Link</span><i aria-hidden="true" class="icon-link-out extlink"></i></a>.</p>
    <p>We want to speak to you in the language that you’re most comfortable with when you call or visit us. Qualified interpreter services, including sign language, are available at no cost, 24 hours a day, 7 days a week during all hours of operations at all points of contact. We do not encourage the use of family, friends or minors as interpreters. Only the services of interpreters and qualified staff are used to provide language assistance. These may include bilingual providers, staff, and healthcare interpreters. In-person, telephone, video, and alternative modes of communication are available. <a target="_self" title="Learn more about interpreter services">Learn more about interpreter services</a>. </p>
    <p>If you would like to report an error in provider or facility information, <a title="Member Services">please contact us</a>.</p>
    <p>Kaiser Permanente enrollees have full and equal access to covered services, including enrollees with disabilities as required under the Federal Americans with Disabilities Act of 1990 and Section 504 of the Rehabilitation Act of 1973.</p>
    <p>Kaiser Permanente uses the same quality, member experience, or cost-related measures to select practitioners and facilities in Marketplace Silver-tier plans as it does for all other Kaiser Foundation Health Plan (KFHP) products and lines of business. Members enrolled in KFHP Marketplace plans have access to all professional, institutional and ancillary health care providers who participate in KFHP plans’ contracted provider network, in accordance with the terms of members’ KFHP plan of coverage. All Kaiser Permanente Medical Group physicians and network physicians are subject to the same quality review processes and certifications.</p>
    <p>Kaiser Permanente uses the same geographic distribution consideration to select hospitals in Marketplace plans as it does for all other Kaiser Foundation Health Plan (KFHP) products and lines of business. Accessibility of medical offices and medical centers in this directory: All Kaiser Permanente facilities are accessible to members.</p>
    </div>
    </div>
    </div>, <div class="header"><div class="container doctors-locations-header" id="container">
    <div>
    <h1 class="regionH1 searchHeader">
    
    
    
    Find doctors and locations
    
    </h1>
    </div>
    <div>
    <div> <p>We know how important it is to find a doctor who's right for you. To choose or change doctors at any time, for any reason, browse our online profiles here by region, or call <a href="/health/care/consumer/locate-our-services/member-services/hours-and-phone-numbers" target="_self" title="Member services">Member services</a> in your area.</p>
    </div>
    </div>
    <div class="searchContent">
    <div> <p><b>Important:</b> If you think you're having a <a target="_self" title="medical or psychiatric emergency">medical or psychiatric emergency</a>, call 911 or go to the nearest hospital. Do not attempt to access emergency care through this website.</p>
    </div>
    </div>
    </div></div>, <div class="container doctors-locations-header" id="container">
    <div>
    <h1 class="regionH1 searchHeader">
    
    
    
    Find doctors and locations
    
    </h1>
    </div>
    <div>
    <div> <p>We know how important it is to find a doctor who's right for you. To choose or change doctors at any time, for any reason, browse our online profiles here by region, or call <a href="/health/care/consumer/locate-our-services/member-services/hours-and-phone-numbers" target="_self" title="Member services">Member services</a> in your area.</p>
    </div>
    </div>
    <div class="searchContent">
    <div> <p><b>Important:</b> If you think you're having a <a target="_self" title="medical or psychiatric emergency">medical or psychiatric emergency</a>, call 911 or go to the nearest hospital. Do not attempt to access emergency care through this website.</p>
    </div>
    </div>
    </div>, <div>
    <h1 class="regionH1 searchHeader">
    
    
    
    Find doctors and locations
    
    </h1>
    </div>, <div>
    <div> <p>We know how important it is to find a doctor who's right for you. To choose or change doctors at any time, for any reason, browse our online profiles here by region, or call <a href="/health/care/consumer/locate-our-services/member-services/hours-and-phone-numbers" target="_self" title="Member services">Member services</a> in your area.</p>
    </div>
    </div>, <div> <p>We know how important it is to find a doctor who's right for you. To choose or change doctors at any time, for any reason, browse our online profiles here by region, or call <a href="/health/care/consumer/locate-our-services/member-services/hours-and-phone-numbers" target="_self" title="Member services">Member services</a> in your area.</p>
    </div>, <div class="searchContent">
    <div> <p><b>Important:</b> If you think you're having a <a target="_self" title="medical or psychiatric emergency">medical or psychiatric emergency</a>, call 911 or go to the nearest hospital. Do not attempt to access emergency care through this website.</p>
    </div>
    </div>, <div> <p><b>Important:</b> If you think you're having a <a target="_self" title="medical or psychiatric emergency">medical or psychiatric emergency</a>, call 911 or go to the nearest hospital. Do not attempt to access emergency care through this website.</p>
    </div>, <div class="search-app">
    <script> 
      	window.aemAuthoredData = {"chooseDoctorLabel":"Choose a doctor now","kpLocationsLabel":"KP locations","errorQuerySearch":"Use letters, numbers, and the following symbols only: ' & * - , / .","planTypeLabel":"Plan type","selectDoctorTitle":"Choose your doctor","phoneLabel":"Phone numbers","doctorsLabel":"doctors","errorHelpDesk":"Please come back later and try again.","keywordLabel":"Hospitals, specialties, doctors' names, or keywords","directionsLabel":"Directions","regionLabel":"Region","systemError":"<p><span> We're sorry, but this feature is not available right now.</span><br>\r\n<br>\r\n<span>Please come back later and try again.</span></p>\r\n","emergencyCareLabel":"Emergency care","hospitalLabel":"Hospital name","cityDrOp":"Select city","availableServicesLabel":"Available services","searchTypeLabel":"Search type","spellCheckLabel":"Did you mean","selectDoctorText":"<p>Having a personal doctor who you connect with is an important part of taking care of your health.</p>\r\n","keywordTest":"Enter search terms","filtersLabel":"FILTERS","errorOutage":"Search isn't available right now. Try again later.","orLabel":"OR","errorDefaultText":"Search configuration is incomplete. Please contact the admin.","servicesLabel":"Services at a glance","island":"Island","urgentCareLabel":"Urgent care","cityLabel":"City","fromYourLocation":"from your location","affBhNo":"English: Affiliate / NCA / BH / No / Not Accepting patients messag","affObNo":"English: Affiliate / NCA / OB / No / Not Accepting patients messag","milesFrom":"From","providerTypeDrOp1":"Select provider type","providerTypeLabel":"Provider type","searchNearCurrentLocation":"Searching near your current location","cq:lastRolledout":"java.util.GregorianCalendar[time=1484694039791,areFieldsSet=true,areAllFieldsSet=true,lenient=false,zone=sun.util.calendar.ZoneInfo[id=\"GMT-08:00\",offset=-28800000,dstSavings=0,useDaylight=false,transitions=0,lastRule=null],firstDayOfWeek=1,minimalDaysInFirstWeek=1,ERA=1,YEAR=2017,MONTH=0,WEEK_OF_YEAR=3,WEEK_OF_MONTH=3,DAY_OF_MONTH=17,DAY_OF_YEAR=17,DAY_OF_WEEK=3,DAY_OF_WEEK_IN_MONTH=3,AM_PM=1,HOUR=3,HOUR_OF_DAY=15,MINUTE=0,SECOND=39,MILLISECOND=791,ZONE_OFFSET=-28800000,DST_OFFSET=0]","noEmergencyCareLabel":"No emergency care","myLocationLabel":"My location","filterLabel":"More filters","readLess":"Read less","readMore":"Read more","keyword":"Keyword","zipCodeLabel":"Enter ZIP Code","privacyError":"<p><span>Privacy: We're sorry, but this feature is not available right now.</span><br>\r\n<br>\r\n<span>Please come back later and try again.</span></p>\r\n","fromZip":"from","distanceDrOp1":"Within 5 miles","distanceLabel":"Distance","searchLocal":"Switch to search by city or ZIP code","searchTitle":"What can we help you find?","kpObYes":"Accepting new patients","searchTypeFacilities":"Locations","zipDigits":"5 digits only","languageLabel":"Language","providerType":"Provider Type","unAvailableServicesLabel":"Unavailable services","selectedFiltersLabel":"Selected Filters","resultsInLabel":"in","errorNoResults":"No results for the following search criteria","lessFiltersLabel":"Less filters","noUrgentCareLabel":"No urgent care","currentLocation":"Near your current location","costsVaryLabel":"*costs may vary","newSearchLabel":"New search","city":"City ","mile":"Mile","resultsForLabel":"for","miles":"Miles","viewFacility":"View this facility","heathPlan":"Health Plan","specificLocationLabel":"Specific location","errorEmptySearch":"Please choose at least one search option and try again.","affiliatePhoneLabel":"Information","departmentLabel":"Department","kpPcpYes":"Accepting new patients","afltFacilityHospital":"Kaiser Permanente Affiliate","islandDrOp1":"Select island","islandLabel":"Island","mapHeader":"Select a location below for more information","doctorResultsTitle":"Doctor search results","locationsLabel":"locations","noPharmacyLabel":"No pharmacy","searchButtonLabel":"Search","affPcpYes":"Accepting new patients","searchTypeDoctors":"Doctors","genderLabel":"Gender","useMyLocation":"Use my location","acceptingNewPatientsLabel":"Accepting New Patients?","withinMiles":"WITHIN {{0}} MILES","locationResultsTitle":"Location search results","switchDoctorsText":"Search doctors","afterHoursLabel":"After hours","affiliateLocationsLabel":"Affiliate locations*","plansLabel":"Plans accepted","milesLabel":"Distance","services":"Services","errorZip":"Enter a valid U.S. ZIP code.","switchLocationsText":"Search locations","errorTechFailure":"We're sorry, but this feature is not available right now.","hoursLabel":"Hours","textIsRich":"[Ljava.lang.String;@4ad442ff","chooseDoctorLink":"https://mydoctor.kaiserpermanente.org/cyd?refUrl=https://members.kaiserpermanente.org/kpweb/medicalstaffdir/entrypage.do","errorSorry":"Search isn't available right now. Try again later.","kpFacilityHospital":"Kaiser Permanente Plan Hospital","searchLocalHi":"Switch to search by city, ZIP code, or island","cq:lastRolledoutBy":"admin","specialtyLabel":"Specialty","moreFiltersLabel":"More filters","infoNotAvailable":"This information is not available at this time.","pharmacyLabel":"Pharmacy","hospitalAffiliationLabel":"Hospital name ","milesFromYourLocation":"from your location","resultsFoundLabel":"found","noTitle":"NO TITLE","noAfterHoursLabel":"No after hours","skipMap":"Skip map","regions":[]};
      	window.fdlRwd = "false";
      </script>
    <app-root>
    <!-- Inlined styles ONLY for spinner.. will be removed once angular is bootstrapped -->
    <style>.loading-container{position:fixed;z-index:999;overflow:show;margin:auto;top:0;left:0;bottom:0;right:0}.loading-container>div.icon-loading{position:absolute;top:50%;left:50%;transform:translate(-50%,-50%)}.loading-container>div.icon-loading:before{background-size:4em;height:4em;width:4em}.loading-container:before{content:'';display:block;position:fixed;top:0;left:0;width:100%;height:100%;background-color:rgba(255,255,255,0.5)}</style>
    <div class="loading-container">
    <div aria-busy="true" aria-label="page loading indicator is visible" aria-live="assertive" class="icon-loading" role="alertdialog">
    <span></span>
    </div>
    </div>
    </app-root>
    </div>, <div class="loading-container">
    <div aria-busy="true" aria-label="page loading indicator is visible" aria-live="assertive" class="icon-loading" role="alertdialog">
    <span></span>
    </div>
    </div>, <div aria-busy="true" aria-label="page loading indicator is visible" aria-live="assertive" class="icon-loading" role="alertdialog">
    <span></span>
    </div>, <div class="footer">
    <hr class="hrLine"/>
    <div class="container doctors-locations-footer" id="container">
    <div class="column-3 marginRemove">
    <h4 class="footer-heading-title desktop">
    	Find Out About
    </h4>
    <a aria-expanded="false" class="footer-heading-title mobile" href="javascript:void(0);">Find Out About</a>
    <ul class="open-list">
    <li>
    <a href="/health/poc?uri=content:ancillary&amp;ctype=help&amp;tid=WPP::LAWR8Y8RR&amp;tname=site_context&amp;rtype=rop" lang="en-US">Help with finding doctors and locations</a>
    </li>
    <li>
    <a href="/health/poc?uri=content:ancillary&amp;ctype=informational&amp;tid=WPP::LAWRKYLZT&amp;tname=site_context&amp;rtype=rop" lang="en-US">Our physicians</a>
    </li>
    <li>
    <a class="external-link" href="https://kpdoc.org/cydKPorgref" lang="en-US">Choosing your doctor<span class="screenreader-only">External Link</span><i aria-hidden="true" class="icon-link-out extlink"></i></a>
    </li>
    <li>
    <a href="/health/poc?uri=content:ancillary&amp;ctype=informational&amp;tid=WPP::LAWRJFNJW&amp;tname=site_context&amp;rtype=rop" lang="en-US">Affiliated providers</a>
    </li>
    <li>
    <a href="/health/poc?uri=content:ancillary&amp;ctype=informational&amp;tid=WPP::OMV1YSA4U&amp;tname=site_context&amp;rtype=rop" lang="en-US">Durable medical equipment</a>
    </li>
    <li>
    <a href="/health/poc?uri=content:ancillary&amp;ctype=informational&amp;tid=WPP::OMV1XY2GD&amp;tname=site_context&amp;rtype=rop" lang="en-US">Breastfeeding counseling and resources</a>
    </li>
    <li>
    <a class="external-link" href="https://kpdoc.org/travelKPorgref" lang="en-US">International travel services <span class="screenreader-only">External Link</span><i aria-hidden="true" class="icon-link-out extlink"></i></a>
    </li>
    <li>
    <a href="/health/poc?uri=content:ancillary&amp;ctype=glossary&amp;tname=site_context&amp;tid=WPP::LAWRA0N6U&amp;rtype=rop" lang="en-US">Glossary</a>
    </li>
    <li>
    <a href="/health/care/consumer/center/!ut/p/a1/hY7Ra8IwGMT_Fh_6GL4v1mSJb42z0patirK5vIyshFqoSShB2X-_ruKjeHBwB8fxAw1H0M5cutbEzjvT_3fNv_NyXytFM6xZzbB4YxtZ8vc5rl7gE0rQbe9_pvHXKcawTDDBawiNd9G62Iy2Q4KgzRC7prdwFIoLmS9WRAgqCaVrSiRbUJIzmSohePaq5NO3W3LmPB6e_JVET1obSWMGO1LpCRzTYjeBb7YcsRDVofqQVYo4vw8eKEMIZ_Gb9pewzmazPwf9OWU!/dl5/d5/L2dBISEvZ0FBIS9nQSEh/" lang="en-US">Timely access to care</a>
    </li>
    </ul>
    </div>
    <div class="column-3 marginRemove">
    <h4 class="footer-heading-title desktop">
    	Related Links
    </h4>
    <a aria-expanded="false" class="footer-heading-title mobile" href="javascript:void(0);">Related Links</a>
    <ul class="open-list">
    <li>
    <a href="/health/poc?uri=content:ancillary&amp;ctype=risk_mitigation&amp;tid=WPP::L6P61N672&amp;tname=site_context&amp;rtype=rop" lang="en-US">What is emergency and urgent care?</a>
    </li>
    <li>
    <a href="/health/mycare/consumer/locate-our-services/member-services/contact-member-services" lang="en-US">Contact Member Services</a>
    </li>
    <li>
    <a href="/health/poc?uri=center:how-to-get-care&amp;article=DE975D32-4514-11E0-BB14-ACCAE9FA5AAA" lang="en-US">How to get care</a>
    </li>
    <li>
    <a href="/health/poc?uri=center:quality-safety" lang="en-US">Quality and safety at KP</a>
    </li>
    <li>
    <a class="external-link" href="http://www.deltadentalins.com/find-a-dentist?d_loc=&amp;d_kw=&amp;d_d=15&amp;d_net=30&amp;d_prg=delta&amp;d_co=delta" lang="en-US">DeltaCare USA network for Eligible Pediatric Enrollees<span class="screenreader-only">External Link</span><i aria-hidden="true" class="icon-link-out extlink"></i></a>
    </li>
    </ul>
    </div>
    <div class="column-6 imp-note">
    <h3 id="expandCollapseTitle"> Your personal doctor </h3>
    <div class="fullText" style="display:none">
    <span>
    <p>An important part of your health care is building a personal relationship with your doctor.</p>
    <p>To select a primary care physician, <a></a><a target="_self" title="search our doctors "></a><a href="https://mydoctor.kaiserpermanente.org/ncal/mdo/#/" title="search our doctors">search our doctors</a> or <a target="_self" title="call us"></a><a href="/health/care/consumer/locate-our-services/member-services/hours-and-phone-numbers" title="call us">call us</a> and we'll help find an available doctor near you.</p>
    <p>To make an appointment or get advice, call 866-454-8855.<br/>
    </p>
    </span>
    </div>
    <div class="shortText"></div>
    <div>
    <a href="#" id="viewmore" style="display:none">More</a>
    </div>
    <div>
    <a href="#" id="viewless" style="display:none">Less</a>
    </div>
    <script>
    	$( document ).ready(function() {
            var $pTag = $("div.fullText").find('span');
    		var shortText = $pTag.html();
    		if(shortText.length >350){
                 shortText = shortText.substring(0,350);
                 $('#viewmore').show();
                 }
            $("div.shortText").append('<p>'+shortText+'</p>');
    	});
    
        $('#viewmore').click(function(e) {
            $('.shortText').hide();
            $('#viewmore').hide();
            $('#viewless').show();
           	$("div.fullText").show();
            e.preventDefault();
         });
    
         $('#viewless').click(function(e)
          {    
          	$('#viewless').hide();
       		$("div.fullText").hide();
          	$('.shortText').show();
            $('#viewmore').show();
            $('#expandCollapseTitle').attr("tabindex",0).focus();
            e.preventDefault();
         });
    </script>
    </div>
    </div>
    <div class="container doctors-locations-disclaimer" id="container">
    <p><b>To find:</b></p>
    <ul>
    <li>a provider's office hours, search our facility directory</li>
    <li>providers in your plan or accepting new patients, call 1-800-464-4000 (toll free) or 711 (TTY for the hearing/speech impaired)</li>
    </ul>
    <p>The information in this online directory is updated periodically. The availability of physicians, hospitals, providers, and services may change. Information about a practitioner is provided to us by the practitioner or is obtained as part of the credentialing process. If you have questions, please call us at 1-800-464-4000 (toll free). For the hearing and speech impaired: 1-800-464-4000 (toll free) or TTY 711 (toll free). You can also call the Medical Board of California at 916-263-2382, or visit <a class="external-link" href="http://www.mbc.ca.gov/" target="_blank" title="their website">their website<span class="screenreader-only">External Link</span><i aria-hidden="true" class="icon-link-out extlink"></i></a>.</p>
    <p>We want to speak to you in the language that you’re most comfortable with when you call or visit us. Qualified interpreter services, including sign language, are available at no cost, 24 hours a day, 7 days a week during all hours of operations at all points of contact. We do not encourage the use of family, friends or minors as interpreters. Only the services of interpreters and qualified staff are used to provide language assistance. These may include bilingual providers, staff, and healthcare interpreters. In-person, telephone, video, and alternative modes of communication are available. <a target="_self" title="Learn more about interpreter services">Learn more about interpreter services</a>. </p>
    <p>If you would like to report an error in provider or facility information, <a title="Member Services">please contact us</a>.</p>
    <p>Kaiser Permanente enrollees have full and equal access to covered services, including enrollees with disabilities as required under the Federal Americans with Disabilities Act of 1990 and Section 504 of the Rehabilitation Act of 1973.</p>
    <p>Kaiser Permanente uses the same quality, member experience, or cost-related measures to select practitioners and facilities in Marketplace Silver-tier plans as it does for all other Kaiser Foundation Health Plan (KFHP) products and lines of business. Members enrolled in KFHP Marketplace plans have access to all professional, institutional and ancillary health care providers who participate in KFHP plans’ contracted provider network, in accordance with the terms of members’ KFHP plan of coverage. All Kaiser Permanente Medical Group physicians and network physicians are subject to the same quality review processes and certifications.</p>
    <p>Kaiser Permanente uses the same geographic distribution consideration to select hospitals in Marketplace plans as it does for all other Kaiser Foundation Health Plan (KFHP) products and lines of business. Accessibility of medical offices and medical centers in this directory: All Kaiser Permanente facilities are accessible to members.</p>
    </div>
    </div>, <div class="container doctors-locations-footer" id="container">
    <div class="column-3 marginRemove">
    <h4 class="footer-heading-title desktop">
    	Find Out About
    </h4>
    <a aria-expanded="false" class="footer-heading-title mobile" href="javascript:void(0);">Find Out About</a>
    <ul class="open-list">
    <li>
    <a href="/health/poc?uri=content:ancillary&amp;ctype=help&amp;tid=WPP::LAWR8Y8RR&amp;tname=site_context&amp;rtype=rop" lang="en-US">Help with finding doctors and locations</a>
    </li>
    <li>
    <a href="/health/poc?uri=content:ancillary&amp;ctype=informational&amp;tid=WPP::LAWRKYLZT&amp;tname=site_context&amp;rtype=rop" lang="en-US">Our physicians</a>
    </li>
    <li>
    <a class="external-link" href="https://kpdoc.org/cydKPorgref" lang="en-US">Choosing your doctor<span class="screenreader-only">External Link</span><i aria-hidden="true" class="icon-link-out extlink"></i></a>
    </li>
    <li>
    <a href="/health/poc?uri=content:ancillary&amp;ctype=informational&amp;tid=WPP::LAWRJFNJW&amp;tname=site_context&amp;rtype=rop" lang="en-US">Affiliated providers</a>
    </li>
    <li>
    <a href="/health/poc?uri=content:ancillary&amp;ctype=informational&amp;tid=WPP::OMV1YSA4U&amp;tname=site_context&amp;rtype=rop" lang="en-US">Durable medical equipment</a>
    </li>
    <li>
    <a href="/health/poc?uri=content:ancillary&amp;ctype=informational&amp;tid=WPP::OMV1XY2GD&amp;tname=site_context&amp;rtype=rop" lang="en-US">Breastfeeding counseling and resources</a>
    </li>
    <li>
    <a class="external-link" href="https://kpdoc.org/travelKPorgref" lang="en-US">International travel services <span class="screenreader-only">External Link</span><i aria-hidden="true" class="icon-link-out extlink"></i></a>
    </li>
    <li>
    <a href="/health/poc?uri=content:ancillary&amp;ctype=glossary&amp;tname=site_context&amp;tid=WPP::LAWRA0N6U&amp;rtype=rop" lang="en-US">Glossary</a>
    </li>
    <li>
    <a href="/health/care/consumer/center/!ut/p/a1/hY7Ra8IwGMT_Fh_6GL4v1mSJb42z0patirK5vIyshFqoSShB2X-_ruKjeHBwB8fxAw1H0M5cutbEzjvT_3fNv_NyXytFM6xZzbB4YxtZ8vc5rl7gE0rQbe9_pvHXKcawTDDBawiNd9G62Iy2Q4KgzRC7prdwFIoLmS9WRAgqCaVrSiRbUJIzmSohePaq5NO3W3LmPB6e_JVET1obSWMGO1LpCRzTYjeBb7YcsRDVofqQVYo4vw8eKEMIZ_Gb9pewzmazPwf9OWU!/dl5/d5/L2dBISEvZ0FBIS9nQSEh/" lang="en-US">Timely access to care</a>
    </li>
    </ul>
    </div>
    <div class="column-3 marginRemove">
    <h4 class="footer-heading-title desktop">
    	Related Links
    </h4>
    <a aria-expanded="false" class="footer-heading-title mobile" href="javascript:void(0);">Related Links</a>
    <ul class="open-list">
    <li>
    <a href="/health/poc?uri=content:ancillary&amp;ctype=risk_mitigation&amp;tid=WPP::L6P61N672&amp;tname=site_context&amp;rtype=rop" lang="en-US">What is emergency and urgent care?</a>
    </li>
    <li>
    <a href="/health/mycare/consumer/locate-our-services/member-services/contact-member-services" lang="en-US">Contact Member Services</a>
    </li>
    <li>
    <a href="/health/poc?uri=center:how-to-get-care&amp;article=DE975D32-4514-11E0-BB14-ACCAE9FA5AAA" lang="en-US">How to get care</a>
    </li>
    <li>
    <a href="/health/poc?uri=center:quality-safety" lang="en-US">Quality and safety at KP</a>
    </li>
    <li>
    <a class="external-link" href="http://www.deltadentalins.com/find-a-dentist?d_loc=&amp;d_kw=&amp;d_d=15&amp;d_net=30&amp;d_prg=delta&amp;d_co=delta" lang="en-US">DeltaCare USA network for Eligible Pediatric Enrollees<span class="screenreader-only">External Link</span><i aria-hidden="true" class="icon-link-out extlink"></i></a>
    </li>
    </ul>
    </div>
    <div class="column-6 imp-note">
    <h3 id="expandCollapseTitle"> Your personal doctor </h3>
    <div class="fullText" style="display:none">
    <span>
    <p>An important part of your health care is building a personal relationship with your doctor.</p>
    <p>To select a primary care physician, <a></a><a target="_self" title="search our doctors "></a><a href="https://mydoctor.kaiserpermanente.org/ncal/mdo/#/" title="search our doctors">search our doctors</a> or <a target="_self" title="call us"></a><a href="/health/care/consumer/locate-our-services/member-services/hours-and-phone-numbers" title="call us">call us</a> and we'll help find an available doctor near you.</p>
    <p>To make an appointment or get advice, call 866-454-8855.<br/>
    </p>
    </span>
    </div>
    <div class="shortText"></div>
    <div>
    <a href="#" id="viewmore" style="display:none">More</a>
    </div>
    <div>
    <a href="#" id="viewless" style="display:none">Less</a>
    </div>
    <script>
    	$( document ).ready(function() {
            var $pTag = $("div.fullText").find('span');
    		var shortText = $pTag.html();
    		if(shortText.length >350){
                 shortText = shortText.substring(0,350);
                 $('#viewmore').show();
                 }
            $("div.shortText").append('<p>'+shortText+'</p>');
    	});
    
        $('#viewmore').click(function(e) {
            $('.shortText').hide();
            $('#viewmore').hide();
            $('#viewless').show();
           	$("div.fullText").show();
            e.preventDefault();
         });
    
         $('#viewless').click(function(e)
          {    
          	$('#viewless').hide();
       		$("div.fullText").hide();
          	$('.shortText').show();
            $('#viewmore').show();
            $('#expandCollapseTitle').attr("tabindex",0).focus();
            e.preventDefault();
         });
    </script>
    </div>
    </div>, <div class="column-3 marginRemove">
    <h4 class="footer-heading-title desktop">
    	Find Out About
    </h4>
    <a aria-expanded="false" class="footer-heading-title mobile" href="javascript:void(0);">Find Out About</a>
    <ul class="open-list">
    <li>
    <a href="/health/poc?uri=content:ancillary&amp;ctype=help&amp;tid=WPP::LAWR8Y8RR&amp;tname=site_context&amp;rtype=rop" lang="en-US">Help with finding doctors and locations</a>
    </li>
    <li>
    <a href="/health/poc?uri=content:ancillary&amp;ctype=informational&amp;tid=WPP::LAWRKYLZT&amp;tname=site_context&amp;rtype=rop" lang="en-US">Our physicians</a>
    </li>
    <li>
    <a class="external-link" href="https://kpdoc.org/cydKPorgref" lang="en-US">Choosing your doctor<span class="screenreader-only">External Link</span><i aria-hidden="true" class="icon-link-out extlink"></i></a>
    </li>
    <li>
    <a href="/health/poc?uri=content:ancillary&amp;ctype=informational&amp;tid=WPP::LAWRJFNJW&amp;tname=site_context&amp;rtype=rop" lang="en-US">Affiliated providers</a>
    </li>
    <li>
    <a href="/health/poc?uri=content:ancillary&amp;ctype=informational&amp;tid=WPP::OMV1YSA4U&amp;tname=site_context&amp;rtype=rop" lang="en-US">Durable medical equipment</a>
    </li>
    <li>
    <a href="/health/poc?uri=content:ancillary&amp;ctype=informational&amp;tid=WPP::OMV1XY2GD&amp;tname=site_context&amp;rtype=rop" lang="en-US">Breastfeeding counseling and resources</a>
    </li>
    <li>
    <a class="external-link" href="https://kpdoc.org/travelKPorgref" lang="en-US">International travel services <span class="screenreader-only">External Link</span><i aria-hidden="true" class="icon-link-out extlink"></i></a>
    </li>
    <li>
    <a href="/health/poc?uri=content:ancillary&amp;ctype=glossary&amp;tname=site_context&amp;tid=WPP::LAWRA0N6U&amp;rtype=rop" lang="en-US">Glossary</a>
    </li>
    <li>
    <a href="/health/care/consumer/center/!ut/p/a1/hY7Ra8IwGMT_Fh_6GL4v1mSJb42z0patirK5vIyshFqoSShB2X-_ruKjeHBwB8fxAw1H0M5cutbEzjvT_3fNv_NyXytFM6xZzbB4YxtZ8vc5rl7gE0rQbe9_pvHXKcawTDDBawiNd9G62Iy2Q4KgzRC7prdwFIoLmS9WRAgqCaVrSiRbUJIzmSohePaq5NO3W3LmPB6e_JVET1obSWMGO1LpCRzTYjeBb7YcsRDVofqQVYo4vw8eKEMIZ_Gb9pewzmazPwf9OWU!/dl5/d5/L2dBISEvZ0FBIS9nQSEh/" lang="en-US">Timely access to care</a>
    </li>
    </ul>
    </div>, <div class="column-3 marginRemove">
    <h4 class="footer-heading-title desktop">
    	Related Links
    </h4>
    <a aria-expanded="false" class="footer-heading-title mobile" href="javascript:void(0);">Related Links</a>
    <ul class="open-list">
    <li>
    <a href="/health/poc?uri=content:ancillary&amp;ctype=risk_mitigation&amp;tid=WPP::L6P61N672&amp;tname=site_context&amp;rtype=rop" lang="en-US">What is emergency and urgent care?</a>
    </li>
    <li>
    <a href="/health/mycare/consumer/locate-our-services/member-services/contact-member-services" lang="en-US">Contact Member Services</a>
    </li>
    <li>
    <a href="/health/poc?uri=center:how-to-get-care&amp;article=DE975D32-4514-11E0-BB14-ACCAE9FA5AAA" lang="en-US">How to get care</a>
    </li>
    <li>
    <a href="/health/poc?uri=center:quality-safety" lang="en-US">Quality and safety at KP</a>
    </li>
    <li>
    <a class="external-link" href="http://www.deltadentalins.com/find-a-dentist?d_loc=&amp;d_kw=&amp;d_d=15&amp;d_net=30&amp;d_prg=delta&amp;d_co=delta" lang="en-US">DeltaCare USA network for Eligible Pediatric Enrollees<span class="screenreader-only">External Link</span><i aria-hidden="true" class="icon-link-out extlink"></i></a>
    </li>
    </ul>
    </div>, <div class="column-6 imp-note">
    <h3 id="expandCollapseTitle"> Your personal doctor </h3>
    <div class="fullText" style="display:none">
    <span>
    <p>An important part of your health care is building a personal relationship with your doctor.</p>
    <p>To select a primary care physician, <a></a><a target="_self" title="search our doctors "></a><a href="https://mydoctor.kaiserpermanente.org/ncal/mdo/#/" title="search our doctors">search our doctors</a> or <a target="_self" title="call us"></a><a href="/health/care/consumer/locate-our-services/member-services/hours-and-phone-numbers" title="call us">call us</a> and we'll help find an available doctor near you.</p>
    <p>To make an appointment or get advice, call 866-454-8855.<br/>
    </p>
    </span>
    </div>
    <div class="shortText"></div>
    <div>
    <a href="#" id="viewmore" style="display:none">More</a>
    </div>
    <div>
    <a href="#" id="viewless" style="display:none">Less</a>
    </div>
    <script>
    	$( document ).ready(function() {
            var $pTag = $("div.fullText").find('span');
    		var shortText = $pTag.html();
    		if(shortText.length >350){
                 shortText = shortText.substring(0,350);
                 $('#viewmore').show();
                 }
            $("div.shortText").append('<p>'+shortText+'</p>');
    	});
    
        $('#viewmore').click(function(e) {
            $('.shortText').hide();
            $('#viewmore').hide();
            $('#viewless').show();
           	$("div.fullText").show();
            e.preventDefault();
         });
    
         $('#viewless').click(function(e)
          {    
          	$('#viewless').hide();
       		$("div.fullText").hide();
          	$('.shortText').show();
            $('#viewmore').show();
            $('#expandCollapseTitle').attr("tabindex",0).focus();
            e.preventDefault();
         });
    </script>
    </div>, <div class="fullText" style="display:none">
    <span>
    <p>An important part of your health care is building a personal relationship with your doctor.</p>
    <p>To select a primary care physician, <a></a><a target="_self" title="search our doctors "></a><a href="https://mydoctor.kaiserpermanente.org/ncal/mdo/#/" title="search our doctors">search our doctors</a> or <a target="_self" title="call us"></a><a href="/health/care/consumer/locate-our-services/member-services/hours-and-phone-numbers" title="call us">call us</a> and we'll help find an available doctor near you.</p>
    <p>To make an appointment or get advice, call 866-454-8855.<br/>
    </p>
    </span>
    </div>, <div class="shortText"></div>, <div>
    <a href="#" id="viewmore" style="display:none">More</a>
    </div>, <div>
    <a href="#" id="viewless" style="display:none">Less</a>
    </div>, <div class="container doctors-locations-disclaimer" id="container">
    <p><b>To find:</b></p>
    <ul>
    <li>a provider's office hours, search our facility directory</li>
    <li>providers in your plan or accepting new patients, call 1-800-464-4000 (toll free) or 711 (TTY for the hearing/speech impaired)</li>
    </ul>
    <p>The information in this online directory is updated periodically. The availability of physicians, hospitals, providers, and services may change. Information about a practitioner is provided to us by the practitioner or is obtained as part of the credentialing process. If you have questions, please call us at 1-800-464-4000 (toll free). For the hearing and speech impaired: 1-800-464-4000 (toll free) or TTY 711 (toll free). You can also call the Medical Board of California at 916-263-2382, or visit <a class="external-link" href="http://www.mbc.ca.gov/" target="_blank" title="their website">their website<span class="screenreader-only">External Link</span><i aria-hidden="true" class="icon-link-out extlink"></i></a>.</p>
    <p>We want to speak to you in the language that you’re most comfortable with when you call or visit us. Qualified interpreter services, including sign language, are available at no cost, 24 hours a day, 7 days a week during all hours of operations at all points of contact. We do not encourage the use of family, friends or minors as interpreters. Only the services of interpreters and qualified staff are used to provide language assistance. These may include bilingual providers, staff, and healthcare interpreters. In-person, telephone, video, and alternative modes of communication are available. <a target="_self" title="Learn more about interpreter services">Learn more about interpreter services</a>. </p>
    <p>If you would like to report an error in provider or facility information, <a title="Member Services">please contact us</a>.</p>
    <p>Kaiser Permanente enrollees have full and equal access to covered services, including enrollees with disabilities as required under the Federal Americans with Disabilities Act of 1990 and Section 504 of the Rehabilitation Act of 1973.</p>
    <p>Kaiser Permanente uses the same quality, member experience, or cost-related measures to select practitioners and facilities in Marketplace Silver-tier plans as it does for all other Kaiser Foundation Health Plan (KFHP) products and lines of business. Members enrolled in KFHP Marketplace plans have access to all professional, institutional and ancillary health care providers who participate in KFHP plans’ contracted provider network, in accordance with the terms of members’ KFHP plan of coverage. All Kaiser Permanente Medical Group physicians and network physicians are subject to the same quality review processes and certifications.</p>
    <p>Kaiser Permanente uses the same geographic distribution consideration to select hospitals in Marketplace plans as it does for all other Kaiser Foundation Health Plan (KFHP) products and lines of business. Accessibility of medical offices and medical centers in this directory: All Kaiser Permanente facilities are accessible to members.</p>
    </div>, <div id="kp-hoverboard"></div>, <div class="kp-footer" data-analytics-location="kp-footer">
    <div class="nav upper four-columns">
    <!-- Footer Navigation Links -->
    <section class="accordion-container">
    <div class="content">
    <h4 class="footer-heading-title desktop">
    	Find Care
    </h4>
    <a aria-controls="get_care" aria-expanded="false" class="footer-heading-title mobile" href="javascript:void(0);">Find Care</a>
    <ul class="open-list" id="get_care">
    <li>
    <a href="/doctors-locations/how-to-find-care/get-advice" lang="en-US">Advice</a>
    </li>
    <li>
    <a href="/doctors-locations/how-to-find-care/routine-care" lang="en-US">Routine Care</a>
    </li>
    <li>
    <a href="/doctors-locations/how-to-find-care/urgent-care" lang="en-US">Urgent Care</a>
    </li>
    <li>
    <a href="/doctors-locations/how-to-find-care/emergency-care" lang="en-US">Emergency Care</a>
    </li>
    <li>
    <a href="/health/care/consumer/locate-our-services/doctors-and-locations" lang="en-US">Find Doctors &amp; Locations</a>
    </li>
    <li>
    <a href="/doctors-locations/how-to-find-care/behavioral-health" lang="en-US">Behavioral Health</a>
    </li>
    <li>
    <a href="/health/care/consumer/health-wellness/programs-classes" lang="en-US">Health Classes</a>
    </li>
    <li>
    <a href="/health/poc?uri=center:travel-health" lang="en-US">When Traveling</a>
    </li>
    <li>
    <a href="/health/poc?uri=center:how-to-get-care&amp;article=8B689F4C-8819-11E1-9541-F593B886ADB9" lang="en-US">Timely Access to Care</a>
    </li>
    </ul>
    </div>
    </section>
    <section class="accordion-container">
    <div class="content">
    <h4 class="footer-heading-title desktop">
    	Our Organization
    </h4>
    <a aria-controls="our_org" aria-expanded="false" class="footer-heading-title mobile" href="javascript:void(0);">Our Organization</a>
    <ul class="open-list" id="our_org">
    <li>
    <a href="/health/poc?uri=center:about-kp">About KP</a>
    </li>
    <li>
    <a href="http://share.kaiserpermanente.org">News &amp; Views</a>
    </li>
    <li>
    <a href="http://share.kaiserpermanente.org/category/about-community-benefit">Commitment to the Community</a>
    </li>
    <li>
    <a href="/health/poc?uri=content:ancillary&amp;ctype=informational&amp;tname=site_context&amp;tid=WPP::LOYOSY40I">Diversity &amp; Inclusion</a>
    </li>
    <li>
    <a href="/health/poc?uri=content:ancillary&amp;ctype=informational&amp;tid=WPP::LJIAW0MN4&amp;tname=site_context">Awards &amp; Accreditations</a>
    </li>
    <li>
    <a href="https://kp.org/annualreport">Annual Report</a>
    </li>
    <li>
    <a href="https://kp.org/careers">Careers</a>
    </li>
    <li>
    <a href="http://share.kaiserpermanente.org/contact-us/media-contacts/">Media Inquiries</a>
    </li>
    </ul>
    </div>
    </section>
    <section class="accordion-container">
    <div class="content">
    <h4 class="footer-heading-title desktop">
    	Member Support
    </h4>
    <a aria-controls="member_support" aria-expanded="false" class="footer-heading-title mobile" href="javascript:void(0);">Member Support</a>
    <ul class="open-list" id="member_support">
    <li>
    <a href="/new-members/">New Member Welcome</a>
    </li>
    <li>
    <a href="/health/poc?uri=center:forms-and-publications">Forms &amp; Publications</a>
    </li>
    <li>
    <a href="/health/care/consumer/member-assistance">Member Assistance</a>
    </li>
    <li>
    <a href="/health/care/consumer/locate-our-services/member-services/">Member Services</a>
    </li>
    <li>
    <a href="/health/poc?uri=center:information-requests&amp;nodeid=WPP::NI51IUJQ2" lang="en-US">Medical information requests</a>
    </li>
    </ul>
    </div>
    </section>
    <section class="accordion-container">
    <div class="content">
    <h4 class="footer-heading-title desktop">
    			Visit Our Other Sites
    		</h4>
    <a aria-controls="visit_other" aria-expanded="false" class="footer-heading-title mobile" href="javascript:void(0);">Visit Our Other Sites</a>
    <ul class="open-list" id="visit_other">
    <li>
    <a href="https://individual-family.kaiserpermanente.org/healthinsurance">Individual &amp; Family Plans</a>
    </li>
    <li>
    <a href="https://thrive.kaiserpermanente.org/medicaid">Medicaid/Medi-Cal</a>
    </li>
    <li>
    <a href="https://medicare.kaiserpermanente.org">Medicare</a>
    </li>
    <li>
    <a href="http://healthreform.kaiserpermanente.org/">Affordable Care Act</a>
    </li>
    <li>
    <a href="https://businesshealth.kaiserpermanente.org">For Businesses</a>
    </li>
    <li>
    <a href="https://account.kp.org/broker-employer/resources/broker">Broker Support</a>
    </li>
    </ul>
    </div>
    <div class="content language-container" id="language-selector">
    <h4 class="language-heading">Language</h4>
    <ul class="open-list" id="fourth-column">
    <li><a data-language="es" data-language-modal="true" data-language-uri="https://espanol.kaiserpermanente.org/es/northern-california/doctors-locations" href="https://espanol.kaiserpermanente.org/es/northern-california/doctors-locations"> Español</a></li>
    <li><i aria-label="Globe Icon" class="icon-globe" role="img"></i><a class="other-language" href="https://kp.org/languages"> Other Languages</a></li>
    </ul>
    </div>
    </section>
    </div>
    <!-- Secondary Footer Menu Links -->
    <div class="lower">
    <div>
    <div class="social-header section">
    <h2 class="follow-text">Follow Us</h2>
    </div>
    <div class="social-links section" role="navigation">
    <ul class="social-icon-list horizontal-list">
    <li><a class="icon-twitter" data-skip-ext-icon="true" href="https://twitter.com/kpthrive" lang="en-US" title="twitter"><span>twitter Icon</span></a></li>
    <li><a class="icon-facebook" data-skip-ext-icon="true" href="https://www.facebook.com/kpthrive" lang="en-US" title="facebook"><span>facebook Icon</span></a></li>
    <li><a class="icon-youtube" data-skip-ext-icon="true" href="http://www.youtube.com/user/kaiserpermanenteorg" lang="en-US" title="youtube"><span>youtube Icon</span></a></li>
    <li><a class="icon-pinterest" data-skip-ext-icon="true" href="https://www.pinterest.com/kpthrive" lang="en-US" title="pinterest"><span>pinterest Icon</span></a></li>
    <li><a class="icon-instagram" data-skip-ext-icon="true" href="https://www.instagram.com/kpthrive/" lang="en-US" title="instagram"><span>instagram Icon</span></a></li>
    </ul>
    </div>
    </div>
    <div>
    <ul class="leg-reg-links horizontal-list -divided" id="secondary_footer_links">
    <li><a href="/health/poc?uri=content:ancillary&amp;ctype=informational&amp;tid=WPP::LXJZXQ4NU&amp;tname=site_context">Accessibility</a></li>
    <li><a href="https://kp.org/notices">Nondiscrimination Notice</a></li>
    <li><a href="/health/poc?uri=center:privacy-statement">Privacy</a></li>
    <li><a href="/health/poc?uri=content:ancillary&amp;ctype=terms_conditions&amp;tid=WPP::KZ39WVLZT&amp;tname=site_context">Terms &amp; Conditions</a></li>
    <li><a href="/health/poc?uri=center:rights-responsibilities">Rights &amp; Responsibilities</a></li>
    <li><a href="/health/poc?uri=center:site-policies">Site Policies</a></li>
    <li><a href="/health/poc?uri=content:ancillary&amp;ctype=informational&amp;tid=WPP::MZ1L3A9B0&amp;tname=site_context">Disaster Planning</a></li>
    <li><a href="/health/poc?uri=center:technical-information">Technical Information</a></li>
    <li><a href="/health/care/consumer/site-map">Site Map</a></li>
    <li><a href="/health/care/consumer/locate-our-services/member-services/contact-web-manager">Contact Site Manager</a></li>
    </ul>
    </div>
    <div class="external-site-link-disclaimer">
    				
        
        
            Selecting these links
            <i aria-label="external site icon" class="icon-link-out extlink" role="img"><span class="screenreader-only">external site icon</span></i>
            will take you away from KP.org. Kaiser Permanente is not responsible for the content or policies of external websites.
            <a href="/termsconditions#links" target="_self">Details</a>
    </div>
    <!-- Footer Copyright -->
    <div class="copyright footer-copy-desktop" x-ms-format-detection="none">
    <p style="line-height: normal;"> </p>
    <p style="line-height: normal;">Kaiser Permanente health plans around the country: Kaiser Foundation Health Plan, Inc., in Northern and Southern California and Hawaii • Kaiser Foundation Health Plan of Colorado • Kaiser Foundation Health Plan of Georgia, Inc., Nine Piedmont Center, 3495 Piedmont Road NE, Atlanta, GA 30305, 404-364-7000 • Kaiser Foundation Health Plan of the Mid-Atlantic States, Inc., in Maryland, Virginia, and Washington, D.C., 2101 E. Jefferson St., Rockville, MD 20852 • Kaiser Foundation Health Plan of the Northwest, 500 NE Multnomah St., Suite 100, Portland, OR 97232 • Kaiser Foundation Health Plan of Washington or Kaiser Foundation Health Plan of Washington Options, Inc., 601 Union St., Suite 3100, Seattle, WA 98101<br/>
    </p>
    <p><a class="external-link" href="https://get.adobe.com/reader/" style="background-color: rgb(238,238,238);">Adobe Acrobat Reader<span class="screenreader-only">External Link</span><i aria-hidden="true" class="icon-link-out extlink"></i></a> is required to read PDFs.<br/>
    </p>
    <p>Copyright © 2018 Kaiser Foundation Health Plan, Inc.</p>
    </div>
    <div class="secondary-copyright footer-copy-mobile">
    <p style="line-height: normal;">Kaiser Permanente health plans around the country: Kaiser Foundation Health Plan, Inc., in Northern and Southern California and Hawaii • Kaiser Foundation Health Plan of Colorado • Kaiser Foundation Health Plan of Georgia, Inc., Nine Piedmont Center, 3495 Piedmont Road NE, Atlanta, GA 30305, 404-364-7000 • Kaiser Foundation Health Plan of the Mid-Atlantic States, Inc., in Maryland, Virginia, and Washington, D.C., 2101 E. Jefferson St., Rockville, MD 20852 • Kaiser Foundation Health Plan of the Northwest, 500 NE Multnomah St., Suite 100, Portland, OR 97232 • Kaiser Foundation Health Plan of Washington or Kaiser Foundation Health Plan of Washington Options, Inc., 601 Union St., Suite 3100, Seattle, WA 98101<br/>
    <br/>
    </p>
    <p>Copyright © 2017 Kaiser Foundation Health Plan, Inc.<br/>
    </p>
    </div>
    <!-- Footer Trustee -->
    <div class="footer-trust-e">
    <a data-skip-ext-icon="true" href="https://privacy.truste.com/privacy-seal/validation?rid=83bcfa89-f6b6-4931-8826-9c6e86322922" target="_blank"><img alt="TRUSTe privacy certification program" src="https://privacy-policy.truste.com/privacy-seal/seal?rid=83bcfa89-f6b6-4931-8826-9c6e86322922"/></a>
    </div>
    </div>
    </div>, <div class="nav upper four-columns">
    <!-- Footer Navigation Links -->
    <section class="accordion-container">
    <div class="content">
    <h4 class="footer-heading-title desktop">
    	Find Care
    </h4>
    <a aria-controls="get_care" aria-expanded="false" class="footer-heading-title mobile" href="javascript:void(0);">Find Care</a>
    <ul class="open-list" id="get_care">
    <li>
    <a href="/doctors-locations/how-to-find-care/get-advice" lang="en-US">Advice</a>
    </li>
    <li>
    <a href="/doctors-locations/how-to-find-care/routine-care" lang="en-US">Routine Care</a>
    </li>
    <li>
    <a href="/doctors-locations/how-to-find-care/urgent-care" lang="en-US">Urgent Care</a>
    </li>
    <li>
    <a href="/doctors-locations/how-to-find-care/emergency-care" lang="en-US">Emergency Care</a>
    </li>
    <li>
    <a href="/health/care/consumer/locate-our-services/doctors-and-locations" lang="en-US">Find Doctors &amp; Locations</a>
    </li>
    <li>
    <a href="/doctors-locations/how-to-find-care/behavioral-health" lang="en-US">Behavioral Health</a>
    </li>
    <li>
    <a href="/health/care/consumer/health-wellness/programs-classes" lang="en-US">Health Classes</a>
    </li>
    <li>
    <a href="/health/poc?uri=center:travel-health" lang="en-US">When Traveling</a>
    </li>
    <li>
    <a href="/health/poc?uri=center:how-to-get-care&amp;article=8B689F4C-8819-11E1-9541-F593B886ADB9" lang="en-US">Timely Access to Care</a>
    </li>
    </ul>
    </div>
    </section>
    <section class="accordion-container">
    <div class="content">
    <h4 class="footer-heading-title desktop">
    	Our Organization
    </h4>
    <a aria-controls="our_org" aria-expanded="false" class="footer-heading-title mobile" href="javascript:void(0);">Our Organization</a>
    <ul class="open-list" id="our_org">
    <li>
    <a href="/health/poc?uri=center:about-kp">About KP</a>
    </li>
    <li>
    <a href="http://share.kaiserpermanente.org">News &amp; Views</a>
    </li>
    <li>
    <a href="http://share.kaiserpermanente.org/category/about-community-benefit">Commitment to the Community</a>
    </li>
    <li>
    <a href="/health/poc?uri=content:ancillary&amp;ctype=informational&amp;tname=site_context&amp;tid=WPP::LOYOSY40I">Diversity &amp; Inclusion</a>
    </li>
    <li>
    <a href="/health/poc?uri=content:ancillary&amp;ctype=informational&amp;tid=WPP::LJIAW0MN4&amp;tname=site_context">Awards &amp; Accreditations</a>
    </li>
    <li>
    <a href="https://kp.org/annualreport">Annual Report</a>
    </li>
    <li>
    <a href="https://kp.org/careers">Careers</a>
    </li>
    <li>
    <a href="http://share.kaiserpermanente.org/contact-us/media-contacts/">Media Inquiries</a>
    </li>
    </ul>
    </div>
    </section>
    <section class="accordion-container">
    <div class="content">
    <h4 class="footer-heading-title desktop">
    	Member Support
    </h4>
    <a aria-controls="member_support" aria-expanded="false" class="footer-heading-title mobile" href="javascript:void(0);">Member Support</a>
    <ul class="open-list" id="member_support">
    <li>
    <a href="/new-members/">New Member Welcome</a>
    </li>
    <li>
    <a href="/health/poc?uri=center:forms-and-publications">Forms &amp; Publications</a>
    </li>
    <li>
    <a href="/health/care/consumer/member-assistance">Member Assistance</a>
    </li>
    <li>
    <a href="/health/care/consumer/locate-our-services/member-services/">Member Services</a>
    </li>
    <li>
    <a href="/health/poc?uri=center:information-requests&amp;nodeid=WPP::NI51IUJQ2" lang="en-US">Medical information requests</a>
    </li>
    </ul>
    </div>
    </section>
    <section class="accordion-container">
    <div class="content">
    <h4 class="footer-heading-title desktop">
    			Visit Our Other Sites
    		</h4>
    <a aria-controls="visit_other" aria-expanded="false" class="footer-heading-title mobile" href="javascript:void(0);">Visit Our Other Sites</a>
    <ul class="open-list" id="visit_other">
    <li>
    <a href="https://individual-family.kaiserpermanente.org/healthinsurance">Individual &amp; Family Plans</a>
    </li>
    <li>
    <a href="https://thrive.kaiserpermanente.org/medicaid">Medicaid/Medi-Cal</a>
    </li>
    <li>
    <a href="https://medicare.kaiserpermanente.org">Medicare</a>
    </li>
    <li>
    <a href="http://healthreform.kaiserpermanente.org/">Affordable Care Act</a>
    </li>
    <li>
    <a href="https://businesshealth.kaiserpermanente.org">For Businesses</a>
    </li>
    <li>
    <a href="https://account.kp.org/broker-employer/resources/broker">Broker Support</a>
    </li>
    </ul>
    </div>
    <div class="content language-container" id="language-selector">
    <h4 class="language-heading">Language</h4>
    <ul class="open-list" id="fourth-column">
    <li><a data-language="es" data-language-modal="true" data-language-uri="https://espanol.kaiserpermanente.org/es/northern-california/doctors-locations" href="https://espanol.kaiserpermanente.org/es/northern-california/doctors-locations"> Español</a></li>
    <li><i aria-label="Globe Icon" class="icon-globe" role="img"></i><a class="other-language" href="https://kp.org/languages"> Other Languages</a></li>
    </ul>
    </div>
    </section>
    </div>, <div class="content">
    <h4 class="footer-heading-title desktop">
    	Find Care
    </h4>
    <a aria-controls="get_care" aria-expanded="false" class="footer-heading-title mobile" href="javascript:void(0);">Find Care</a>
    <ul class="open-list" id="get_care">
    <li>
    <a href="/doctors-locations/how-to-find-care/get-advice" lang="en-US">Advice</a>
    </li>
    <li>
    <a href="/doctors-locations/how-to-find-care/routine-care" lang="en-US">Routine Care</a>
    </li>
    <li>
    <a href="/doctors-locations/how-to-find-care/urgent-care" lang="en-US">Urgent Care</a>
    </li>
    <li>
    <a href="/doctors-locations/how-to-find-care/emergency-care" lang="en-US">Emergency Care</a>
    </li>
    <li>
    <a href="/health/care/consumer/locate-our-services/doctors-and-locations" lang="en-US">Find Doctors &amp; Locations</a>
    </li>
    <li>
    <a href="/doctors-locations/how-to-find-care/behavioral-health" lang="en-US">Behavioral Health</a>
    </li>
    <li>
    <a href="/health/care/consumer/health-wellness/programs-classes" lang="en-US">Health Classes</a>
    </li>
    <li>
    <a href="/health/poc?uri=center:travel-health" lang="en-US">When Traveling</a>
    </li>
    <li>
    <a href="/health/poc?uri=center:how-to-get-care&amp;article=8B689F4C-8819-11E1-9541-F593B886ADB9" lang="en-US">Timely Access to Care</a>
    </li>
    </ul>
    </div>, <div class="content">
    <h4 class="footer-heading-title desktop">
    	Our Organization
    </h4>
    <a aria-controls="our_org" aria-expanded="false" class="footer-heading-title mobile" href="javascript:void(0);">Our Organization</a>
    <ul class="open-list" id="our_org">
    <li>
    <a href="/health/poc?uri=center:about-kp">About KP</a>
    </li>
    <li>
    <a href="http://share.kaiserpermanente.org">News &amp; Views</a>
    </li>
    <li>
    <a href="http://share.kaiserpermanente.org/category/about-community-benefit">Commitment to the Community</a>
    </li>
    <li>
    <a href="/health/poc?uri=content:ancillary&amp;ctype=informational&amp;tname=site_context&amp;tid=WPP::LOYOSY40I">Diversity &amp; Inclusion</a>
    </li>
    <li>
    <a href="/health/poc?uri=content:ancillary&amp;ctype=informational&amp;tid=WPP::LJIAW0MN4&amp;tname=site_context">Awards &amp; Accreditations</a>
    </li>
    <li>
    <a href="https://kp.org/annualreport">Annual Report</a>
    </li>
    <li>
    <a href="https://kp.org/careers">Careers</a>
    </li>
    <li>
    <a href="http://share.kaiserpermanente.org/contact-us/media-contacts/">Media Inquiries</a>
    </li>
    </ul>
    </div>, <div class="content">
    <h4 class="footer-heading-title desktop">
    	Member Support
    </h4>
    <a aria-controls="member_support" aria-expanded="false" class="footer-heading-title mobile" href="javascript:void(0);">Member Support</a>
    <ul class="open-list" id="member_support">
    <li>
    <a href="/new-members/">New Member Welcome</a>
    </li>
    <li>
    <a href="/health/poc?uri=center:forms-and-publications">Forms &amp; Publications</a>
    </li>
    <li>
    <a href="/health/care/consumer/member-assistance">Member Assistance</a>
    </li>
    <li>
    <a href="/health/care/consumer/locate-our-services/member-services/">Member Services</a>
    </li>
    <li>
    <a href="/health/poc?uri=center:information-requests&amp;nodeid=WPP::NI51IUJQ2" lang="en-US">Medical information requests</a>
    </li>
    </ul>
    </div>, <div class="content">
    <h4 class="footer-heading-title desktop">
    			Visit Our Other Sites
    		</h4>
    <a aria-controls="visit_other" aria-expanded="false" class="footer-heading-title mobile" href="javascript:void(0);">Visit Our Other Sites</a>
    <ul class="open-list" id="visit_other">
    <li>
    <a href="https://individual-family.kaiserpermanente.org/healthinsurance">Individual &amp; Family Plans</a>
    </li>
    <li>
    <a href="https://thrive.kaiserpermanente.org/medicaid">Medicaid/Medi-Cal</a>
    </li>
    <li>
    <a href="https://medicare.kaiserpermanente.org">Medicare</a>
    </li>
    <li>
    <a href="http://healthreform.kaiserpermanente.org/">Affordable Care Act</a>
    </li>
    <li>
    <a href="https://businesshealth.kaiserpermanente.org">For Businesses</a>
    </li>
    <li>
    <a href="https://account.kp.org/broker-employer/resources/broker">Broker Support</a>
    </li>
    </ul>
    </div>, <div class="content language-container" id="language-selector">
    <h4 class="language-heading">Language</h4>
    <ul class="open-list" id="fourth-column">
    <li><a data-language="es" data-language-modal="true" data-language-uri="https://espanol.kaiserpermanente.org/es/northern-california/doctors-locations" href="https://espanol.kaiserpermanente.org/es/northern-california/doctors-locations"> Español</a></li>
    <li><i aria-label="Globe Icon" class="icon-globe" role="img"></i><a class="other-language" href="https://kp.org/languages"> Other Languages</a></li>
    </ul>
    </div>, <div class="lower">
    <div>
    <div class="social-header section">
    <h2 class="follow-text">Follow Us</h2>
    </div>
    <div class="social-links section" role="navigation">
    <ul class="social-icon-list horizontal-list">
    <li><a class="icon-twitter" data-skip-ext-icon="true" href="https://twitter.com/kpthrive" lang="en-US" title="twitter"><span>twitter Icon</span></a></li>
    <li><a class="icon-facebook" data-skip-ext-icon="true" href="https://www.facebook.com/kpthrive" lang="en-US" title="facebook"><span>facebook Icon</span></a></li>
    <li><a class="icon-youtube" data-skip-ext-icon="true" href="http://www.youtube.com/user/kaiserpermanenteorg" lang="en-US" title="youtube"><span>youtube Icon</span></a></li>
    <li><a class="icon-pinterest" data-skip-ext-icon="true" href="https://www.pinterest.com/kpthrive" lang="en-US" title="pinterest"><span>pinterest Icon</span></a></li>
    <li><a class="icon-instagram" data-skip-ext-icon="true" href="https://www.instagram.com/kpthrive/" lang="en-US" title="instagram"><span>instagram Icon</span></a></li>
    </ul>
    </div>
    </div>
    <div>
    <ul class="leg-reg-links horizontal-list -divided" id="secondary_footer_links">
    <li><a href="/health/poc?uri=content:ancillary&amp;ctype=informational&amp;tid=WPP::LXJZXQ4NU&amp;tname=site_context">Accessibility</a></li>
    <li><a href="https://kp.org/notices">Nondiscrimination Notice</a></li>
    <li><a href="/health/poc?uri=center:privacy-statement">Privacy</a></li>
    <li><a href="/health/poc?uri=content:ancillary&amp;ctype=terms_conditions&amp;tid=WPP::KZ39WVLZT&amp;tname=site_context">Terms &amp; Conditions</a></li>
    <li><a href="/health/poc?uri=center:rights-responsibilities">Rights &amp; Responsibilities</a></li>
    <li><a href="/health/poc?uri=center:site-policies">Site Policies</a></li>
    <li><a href="/health/poc?uri=content:ancillary&amp;ctype=informational&amp;tid=WPP::MZ1L3A9B0&amp;tname=site_context">Disaster Planning</a></li>
    <li><a href="/health/poc?uri=center:technical-information">Technical Information</a></li>
    <li><a href="/health/care/consumer/site-map">Site Map</a></li>
    <li><a href="/health/care/consumer/locate-our-services/member-services/contact-web-manager">Contact Site Manager</a></li>
    </ul>
    </div>
    <div class="external-site-link-disclaimer">
    				
        
        
            Selecting these links
            <i aria-label="external site icon" class="icon-link-out extlink" role="img"><span class="screenreader-only">external site icon</span></i>
            will take you away from KP.org. Kaiser Permanente is not responsible for the content or policies of external websites.
            <a href="/termsconditions#links" target="_self">Details</a>
    </div>
    <!-- Footer Copyright -->
    <div class="copyright footer-copy-desktop" x-ms-format-detection="none">
    <p style="line-height: normal;"> </p>
    <p style="line-height: normal;">Kaiser Permanente health plans around the country: Kaiser Foundation Health Plan, Inc., in Northern and Southern California and Hawaii • Kaiser Foundation Health Plan of Colorado • Kaiser Foundation Health Plan of Georgia, Inc., Nine Piedmont Center, 3495 Piedmont Road NE, Atlanta, GA 30305, 404-364-7000 • Kaiser Foundation Health Plan of the Mid-Atlantic States, Inc., in Maryland, Virginia, and Washington, D.C., 2101 E. Jefferson St., Rockville, MD 20852 • Kaiser Foundation Health Plan of the Northwest, 500 NE Multnomah St., Suite 100, Portland, OR 97232 • Kaiser Foundation Health Plan of Washington or Kaiser Foundation Health Plan of Washington Options, Inc., 601 Union St., Suite 3100, Seattle, WA 98101<br/>
    </p>
    <p><a class="external-link" href="https://get.adobe.com/reader/" style="background-color: rgb(238,238,238);">Adobe Acrobat Reader<span class="screenreader-only">External Link</span><i aria-hidden="true" class="icon-link-out extlink"></i></a> is required to read PDFs.<br/>
    </p>
    <p>Copyright © 2018 Kaiser Foundation Health Plan, Inc.</p>
    </div>
    <div class="secondary-copyright footer-copy-mobile">
    <p style="line-height: normal;">Kaiser Permanente health plans around the country: Kaiser Foundation Health Plan, Inc., in Northern and Southern California and Hawaii • Kaiser Foundation Health Plan of Colorado • Kaiser Foundation Health Plan of Georgia, Inc., Nine Piedmont Center, 3495 Piedmont Road NE, Atlanta, GA 30305, 404-364-7000 • Kaiser Foundation Health Plan of the Mid-Atlantic States, Inc., in Maryland, Virginia, and Washington, D.C., 2101 E. Jefferson St., Rockville, MD 20852 • Kaiser Foundation Health Plan of the Northwest, 500 NE Multnomah St., Suite 100, Portland, OR 97232 • Kaiser Foundation Health Plan of Washington or Kaiser Foundation Health Plan of Washington Options, Inc., 601 Union St., Suite 3100, Seattle, WA 98101<br/>
    <br/>
    </p>
    <p>Copyright © 2017 Kaiser Foundation Health Plan, Inc.<br/>
    </p>
    </div>
    <!-- Footer Trustee -->
    <div class="footer-trust-e">
    <a data-skip-ext-icon="true" href="https://privacy.truste.com/privacy-seal/validation?rid=83bcfa89-f6b6-4931-8826-9c6e86322922" target="_blank"><img alt="TRUSTe privacy certification program" src="https://privacy-policy.truste.com/privacy-seal/seal?rid=83bcfa89-f6b6-4931-8826-9c6e86322922"/></a>
    </div>
    </div>, <div>
    <div class="social-header section">
    <h2 class="follow-text">Follow Us</h2>
    </div>
    <div class="social-links section" role="navigation">
    <ul class="social-icon-list horizontal-list">
    <li><a class="icon-twitter" data-skip-ext-icon="true" href="https://twitter.com/kpthrive" lang="en-US" title="twitter"><span>twitter Icon</span></a></li>
    <li><a class="icon-facebook" data-skip-ext-icon="true" href="https://www.facebook.com/kpthrive" lang="en-US" title="facebook"><span>facebook Icon</span></a></li>
    <li><a class="icon-youtube" data-skip-ext-icon="true" href="http://www.youtube.com/user/kaiserpermanenteorg" lang="en-US" title="youtube"><span>youtube Icon</span></a></li>
    <li><a class="icon-pinterest" data-skip-ext-icon="true" href="https://www.pinterest.com/kpthrive" lang="en-US" title="pinterest"><span>pinterest Icon</span></a></li>
    <li><a class="icon-instagram" data-skip-ext-icon="true" href="https://www.instagram.com/kpthrive/" lang="en-US" title="instagram"><span>instagram Icon</span></a></li>
    </ul>
    </div>
    </div>, <div class="social-header section">
    <h2 class="follow-text">Follow Us</h2>
    </div>, <div class="social-links section" role="navigation">
    <ul class="social-icon-list horizontal-list">
    <li><a class="icon-twitter" data-skip-ext-icon="true" href="https://twitter.com/kpthrive" lang="en-US" title="twitter"><span>twitter Icon</span></a></li>
    <li><a class="icon-facebook" data-skip-ext-icon="true" href="https://www.facebook.com/kpthrive" lang="en-US" title="facebook"><span>facebook Icon</span></a></li>
    <li><a class="icon-youtube" data-skip-ext-icon="true" href="http://www.youtube.com/user/kaiserpermanenteorg" lang="en-US" title="youtube"><span>youtube Icon</span></a></li>
    <li><a class="icon-pinterest" data-skip-ext-icon="true" href="https://www.pinterest.com/kpthrive" lang="en-US" title="pinterest"><span>pinterest Icon</span></a></li>
    <li><a class="icon-instagram" data-skip-ext-icon="true" href="https://www.instagram.com/kpthrive/" lang="en-US" title="instagram"><span>instagram Icon</span></a></li>
    </ul>
    </div>, <div>
    <ul class="leg-reg-links horizontal-list -divided" id="secondary_footer_links">
    <li><a href="/health/poc?uri=content:ancillary&amp;ctype=informational&amp;tid=WPP::LXJZXQ4NU&amp;tname=site_context">Accessibility</a></li>
    <li><a href="https://kp.org/notices">Nondiscrimination Notice</a></li>
    <li><a href="/health/poc?uri=center:privacy-statement">Privacy</a></li>
    <li><a href="/health/poc?uri=content:ancillary&amp;ctype=terms_conditions&amp;tid=WPP::KZ39WVLZT&amp;tname=site_context">Terms &amp; Conditions</a></li>
    <li><a href="/health/poc?uri=center:rights-responsibilities">Rights &amp; Responsibilities</a></li>
    <li><a href="/health/poc?uri=center:site-policies">Site Policies</a></li>
    <li><a href="/health/poc?uri=content:ancillary&amp;ctype=informational&amp;tid=WPP::MZ1L3A9B0&amp;tname=site_context">Disaster Planning</a></li>
    <li><a href="/health/poc?uri=center:technical-information">Technical Information</a></li>
    <li><a href="/health/care/consumer/site-map">Site Map</a></li>
    <li><a href="/health/care/consumer/locate-our-services/member-services/contact-web-manager">Contact Site Manager</a></li>
    </ul>
    </div>, <div class="external-site-link-disclaimer">
    				
        
        
            Selecting these links
            <i aria-label="external site icon" class="icon-link-out extlink" role="img"><span class="screenreader-only">external site icon</span></i>
            will take you away from KP.org. Kaiser Permanente is not responsible for the content or policies of external websites.
            <a href="/termsconditions#links" target="_self">Details</a>
    </div>, <div class="copyright footer-copy-desktop" x-ms-format-detection="none">
    <p style="line-height: normal;"> </p>
    <p style="line-height: normal;">Kaiser Permanente health plans around the country: Kaiser Foundation Health Plan, Inc., in Northern and Southern California and Hawaii • Kaiser Foundation Health Plan of Colorado • Kaiser Foundation Health Plan of Georgia, Inc., Nine Piedmont Center, 3495 Piedmont Road NE, Atlanta, GA 30305, 404-364-7000 • Kaiser Foundation Health Plan of the Mid-Atlantic States, Inc., in Maryland, Virginia, and Washington, D.C., 2101 E. Jefferson St., Rockville, MD 20852 • Kaiser Foundation Health Plan of the Northwest, 500 NE Multnomah St., Suite 100, Portland, OR 97232 • Kaiser Foundation Health Plan of Washington or Kaiser Foundation Health Plan of Washington Options, Inc., 601 Union St., Suite 3100, Seattle, WA 98101<br/>
    </p>
    <p><a class="external-link" href="https://get.adobe.com/reader/" style="background-color: rgb(238,238,238);">Adobe Acrobat Reader<span class="screenreader-only">External Link</span><i aria-hidden="true" class="icon-link-out extlink"></i></a> is required to read PDFs.<br/>
    </p>
    <p>Copyright © 2018 Kaiser Foundation Health Plan, Inc.</p>
    </div>, <div class="secondary-copyright footer-copy-mobile">
    <p style="line-height: normal;">Kaiser Permanente health plans around the country: Kaiser Foundation Health Plan, Inc., in Northern and Southern California and Hawaii • Kaiser Foundation Health Plan of Colorado • Kaiser Foundation Health Plan of Georgia, Inc., Nine Piedmont Center, 3495 Piedmont Road NE, Atlanta, GA 30305, 404-364-7000 • Kaiser Foundation Health Plan of the Mid-Atlantic States, Inc., in Maryland, Virginia, and Washington, D.C., 2101 E. Jefferson St., Rockville, MD 20852 • Kaiser Foundation Health Plan of the Northwest, 500 NE Multnomah St., Suite 100, Portland, OR 97232 • Kaiser Foundation Health Plan of Washington or Kaiser Foundation Health Plan of Washington Options, Inc., 601 Union St., Suite 3100, Seattle, WA 98101<br/>
    <br/>
    </p>
    <p>Copyright © 2017 Kaiser Foundation Health Plan, Inc.<br/>
    </p>
    </div>, <div class="footer-trust-e">
    <a data-skip-ext-icon="true" href="https://privacy.truste.com/privacy-seal/validation?rid=83bcfa89-f6b6-4931-8826-9c6e86322922" target="_blank"><img alt="TRUSTe privacy certification program" src="https://privacy-policy.truste.com/privacy-seal/seal?rid=83bcfa89-f6b6-4931-8826-9c6e86322922"/></a>
    </div>, <div class="kp-foundation-modal">
    <div>
    <div aria-describedby="language-modal-description" aria-labelledby="language-modal-title" class="global-language-modal kp-modal" data-language-modal-container="" id="global-language-modal-id" lang="es-US" role="dialog">
    <div class="modal-fade-screen">
    <div class="modal-inner" role="document" tabindex="-1">
    <button class="-close" id="modal-close">
    <span class="screenreader-only">close modal</span>
    </button>
    <header class="modal-header">
    <h2 id="language-modal-title" tabindex="-1">Importante</h2>
    </header>
    <div class="modal-content" id="language-modal-description" tabindex="-1">
    <p>Usted ha elegido ver nuestro sitio web en español.</p>
    <p>Estamos trabajando para que más funciones estén disponibles en español. Sin embargo, algunas páginas y funciones solo aparecen en inglés.</p>
    <div class="language-modal-checkbox-container"><input aria-labelledby="language-checkbox-label" class="form-control" id="language-checkbox-toggle" type="checkbox"/><label for="language-checkbox-toggle" id="language-checkbox-label">No volver a mostrar esto.</label></div>
    </div>
    <div class="modal-buttons ada-buttons-desktop">
    <button class="button -action" id="language-modal-button-cancel">
    	            Cancelar
    	          </button>
    <button class="button -action -inverted" id="language-modal-button-continue">
    	             Continuar
    	          </button>
    </div>
    <div class="modal-buttons ada-buttons-mobile">
    <button class="button -action -inverted" id="language-modal-button-continue">
    	             Continuar
    	          </button>
    <button class="button -action" id="language-modal-button-cancel">
    	            Cancelar
    	          </button>
    </div>
    </div>
    </div>
    </div>
    </div>
    <div>
    <div aria-describedby="region-modal-description" aria-labelledby="region-modal-title" class="global-region-modal kp-modal" data-disable-modal="true" data-region-modal-container="" id="global-region-modal-id" lang="en-US" role="dialog">
    <div class="modal-fade-screen">
    <div class="modal-inner" role="document" tabindex="-1">
    <button class="-close" id="global-region-modal-close">
    <span class="screenreader-only">close regional modal</span>
    </button>
    <header class="modal-header">
    <h2 id="region-modal-title" tabindex="0">Choose your region</h2>
    </header>
    <div class="modal-content" id="region-modal-description">
    <p>Select your region from the list below.</p>
    <nav class="region-select-radio-options" data-analytics-location="region-picker-modal">
    <fieldset>
    <legend>Regions</legend>
    <input class="radio-button" data-region-id="MRN" id="region-code-MRN" name="region-input-radio-select" type="radio" value="/northern-california/doctors-locations"/>
    <label for="region-code-MRN">California - Northern </label> <br/>
    <input class="radio-button" data-region-id="SCA" id="region-code-SCA" name="region-input-radio-select" type="radio" value="/southern-california/doctors-locations"/>
    <label for="region-code-SCA">California - Southern</label> <br/>
    <input class="radio-button" data-region-id="DB" id="region-code-DB" name="region-input-radio-select" type="radio" value="/colorado-denver-boulder-mountain-northern/doctors-locations"/>
    <label for="region-code-DB">Colorado - Denver / Boulder / Northern / Mountain areas</label> <br/>
    <input class="radio-button" data-region-id="CS" id="region-code-CS" name="region-input-radio-select" type="radio" value="/southern-colorado/doctors-locations"/>
    <label for="region-code-CS">Colorado - Southern </label> <br/>
    <input class="radio-button" data-region-id="GGA" id="region-code-GGA" name="region-input-radio-select" type="radio" value="/georgia/doctors-locations"/>
    <label for="region-code-GGA">Georgia</label> <br/>
    <input class="radio-button" data-region-id="HAW" id="region-code-HAW" name="region-input-radio-select" type="radio" value="/hawaii/doctors-locations"/>
    <label for="region-code-HAW">Hawaii</label> <br/>
    <input class="radio-button" data-region-id="MID" id="region-code-MID" name="region-input-radio-select" type="radio" value="/maryland-virginia-washington-dc/doctors-locations"/>
    <label for="region-code-MID">Maryland / Virginia / Washington, D.C.</label> <br/>
    <input class="radio-button" data-region-id="KNW" id="region-code-KNW" name="region-input-radio-select" type="radio" value="/oregon-washington/doctors-locations"/>
    <label for="region-code-KNW">Oregon / Washington</label> <br/>
    </fieldset>
    </nav>
    </div>
    <div class="modal-buttons ada-buttons-desktop">
    <button class="button -action" id="region-modal-button-cancel">
                Cancel
              </button>
    <button class="button -disabled" disabled="true" id="region-modal-button-continue">
                 Continue
              </button>
    </div>
    <div class="modal-buttons ada-buttons-mobile">
    <button class="button -disabled" disabled="true" id="region-modal-button-continue">
                 Continue
              </button>
    <button class="button -action" id="region-modal-button-cancel">
                Cancel
              </button>
    </div>
    </div>
    </div>
    </div>
    </div>
    </div>, <div>
    <div aria-describedby="language-modal-description" aria-labelledby="language-modal-title" class="global-language-modal kp-modal" data-language-modal-container="" id="global-language-modal-id" lang="es-US" role="dialog">
    <div class="modal-fade-screen">
    <div class="modal-inner" role="document" tabindex="-1">
    <button class="-close" id="modal-close">
    <span class="screenreader-only">close modal</span>
    </button>
    <header class="modal-header">
    <h2 id="language-modal-title" tabindex="-1">Importante</h2>
    </header>
    <div class="modal-content" id="language-modal-description" tabindex="-1">
    <p>Usted ha elegido ver nuestro sitio web en español.</p>
    <p>Estamos trabajando para que más funciones estén disponibles en español. Sin embargo, algunas páginas y funciones solo aparecen en inglés.</p>
    <div class="language-modal-checkbox-container"><input aria-labelledby="language-checkbox-label" class="form-control" id="language-checkbox-toggle" type="checkbox"/><label for="language-checkbox-toggle" id="language-checkbox-label">No volver a mostrar esto.</label></div>
    </div>
    <div class="modal-buttons ada-buttons-desktop">
    <button class="button -action" id="language-modal-button-cancel">
    	            Cancelar
    	          </button>
    <button class="button -action -inverted" id="language-modal-button-continue">
    	             Continuar
    	          </button>
    </div>
    <div class="modal-buttons ada-buttons-mobile">
    <button class="button -action -inverted" id="language-modal-button-continue">
    	             Continuar
    	          </button>
    <button class="button -action" id="language-modal-button-cancel">
    	            Cancelar
    	          </button>
    </div>
    </div>
    </div>
    </div>
    </div>, <div aria-describedby="language-modal-description" aria-labelledby="language-modal-title" class="global-language-modal kp-modal" data-language-modal-container="" id="global-language-modal-id" lang="es-US" role="dialog">
    <div class="modal-fade-screen">
    <div class="modal-inner" role="document" tabindex="-1">
    <button class="-close" id="modal-close">
    <span class="screenreader-only">close modal</span>
    </button>
    <header class="modal-header">
    <h2 id="language-modal-title" tabindex="-1">Importante</h2>
    </header>
    <div class="modal-content" id="language-modal-description" tabindex="-1">
    <p>Usted ha elegido ver nuestro sitio web en español.</p>
    <p>Estamos trabajando para que más funciones estén disponibles en español. Sin embargo, algunas páginas y funciones solo aparecen en inglés.</p>
    <div class="language-modal-checkbox-container"><input aria-labelledby="language-checkbox-label" class="form-control" id="language-checkbox-toggle" type="checkbox"/><label for="language-checkbox-toggle" id="language-checkbox-label">No volver a mostrar esto.</label></div>
    </div>
    <div class="modal-buttons ada-buttons-desktop">
    <button class="button -action" id="language-modal-button-cancel">
    	            Cancelar
    	          </button>
    <button class="button -action -inverted" id="language-modal-button-continue">
    	             Continuar
    	          </button>
    </div>
    <div class="modal-buttons ada-buttons-mobile">
    <button class="button -action -inverted" id="language-modal-button-continue">
    	             Continuar
    	          </button>
    <button class="button -action" id="language-modal-button-cancel">
    	            Cancelar
    	          </button>
    </div>
    </div>
    </div>
    </div>, <div class="modal-fade-screen">
    <div class="modal-inner" role="document" tabindex="-1">
    <button class="-close" id="modal-close">
    <span class="screenreader-only">close modal</span>
    </button>
    <header class="modal-header">
    <h2 id="language-modal-title" tabindex="-1">Importante</h2>
    </header>
    <div class="modal-content" id="language-modal-description" tabindex="-1">
    <p>Usted ha elegido ver nuestro sitio web en español.</p>
    <p>Estamos trabajando para que más funciones estén disponibles en español. Sin embargo, algunas páginas y funciones solo aparecen en inglés.</p>
    <div class="language-modal-checkbox-container"><input aria-labelledby="language-checkbox-label" class="form-control" id="language-checkbox-toggle" type="checkbox"/><label for="language-checkbox-toggle" id="language-checkbox-label">No volver a mostrar esto.</label></div>
    </div>
    <div class="modal-buttons ada-buttons-desktop">
    <button class="button -action" id="language-modal-button-cancel">
    	            Cancelar
    	          </button>
    <button class="button -action -inverted" id="language-modal-button-continue">
    	             Continuar
    	          </button>
    </div>
    <div class="modal-buttons ada-buttons-mobile">
    <button class="button -action -inverted" id="language-modal-button-continue">
    	             Continuar
    	          </button>
    <button class="button -action" id="language-modal-button-cancel">
    	            Cancelar
    	          </button>
    </div>
    </div>
    </div>, <div class="modal-inner" role="document" tabindex="-1">
    <button class="-close" id="modal-close">
    <span class="screenreader-only">close modal</span>
    </button>
    <header class="modal-header">
    <h2 id="language-modal-title" tabindex="-1">Importante</h2>
    </header>
    <div class="modal-content" id="language-modal-description" tabindex="-1">
    <p>Usted ha elegido ver nuestro sitio web en español.</p>
    <p>Estamos trabajando para que más funciones estén disponibles en español. Sin embargo, algunas páginas y funciones solo aparecen en inglés.</p>
    <div class="language-modal-checkbox-container"><input aria-labelledby="language-checkbox-label" class="form-control" id="language-checkbox-toggle" type="checkbox"/><label for="language-checkbox-toggle" id="language-checkbox-label">No volver a mostrar esto.</label></div>
    </div>
    <div class="modal-buttons ada-buttons-desktop">
    <button class="button -action" id="language-modal-button-cancel">
    	            Cancelar
    	          </button>
    <button class="button -action -inverted" id="language-modal-button-continue">
    	             Continuar
    	          </button>
    </div>
    <div class="modal-buttons ada-buttons-mobile">
    <button class="button -action -inverted" id="language-modal-button-continue">
    	             Continuar
    	          </button>
    <button class="button -action" id="language-modal-button-cancel">
    	            Cancelar
    	          </button>
    </div>
    </div>, <div class="modal-content" id="language-modal-description" tabindex="-1">
    <p>Usted ha elegido ver nuestro sitio web en español.</p>
    <p>Estamos trabajando para que más funciones estén disponibles en español. Sin embargo, algunas páginas y funciones solo aparecen en inglés.</p>
    <div class="language-modal-checkbox-container"><input aria-labelledby="language-checkbox-label" class="form-control" id="language-checkbox-toggle" type="checkbox"/><label for="language-checkbox-toggle" id="language-checkbox-label">No volver a mostrar esto.</label></div>
    </div>, <div class="language-modal-checkbox-container"><input aria-labelledby="language-checkbox-label" class="form-control" id="language-checkbox-toggle" type="checkbox"/><label for="language-checkbox-toggle" id="language-checkbox-label">No volver a mostrar esto.</label></div>, <div class="modal-buttons ada-buttons-desktop">
    <button class="button -action" id="language-modal-button-cancel">
    	            Cancelar
    	          </button>
    <button class="button -action -inverted" id="language-modal-button-continue">
    	             Continuar
    	          </button>
    </div>, <div class="modal-buttons ada-buttons-mobile">
    <button class="button -action -inverted" id="language-modal-button-continue">
    	             Continuar
    	          </button>
    <button class="button -action" id="language-modal-button-cancel">
    	            Cancelar
    	          </button>
    </div>, <div>
    <div aria-describedby="region-modal-description" aria-labelledby="region-modal-title" class="global-region-modal kp-modal" data-disable-modal="true" data-region-modal-container="" id="global-region-modal-id" lang="en-US" role="dialog">
    <div class="modal-fade-screen">
    <div class="modal-inner" role="document" tabindex="-1">
    <button class="-close" id="global-region-modal-close">
    <span class="screenreader-only">close regional modal</span>
    </button>
    <header class="modal-header">
    <h2 id="region-modal-title" tabindex="0">Choose your region</h2>
    </header>
    <div class="modal-content" id="region-modal-description">
    <p>Select your region from the list below.</p>
    <nav class="region-select-radio-options" data-analytics-location="region-picker-modal">
    <fieldset>
    <legend>Regions</legend>
    <input class="radio-button" data-region-id="MRN" id="region-code-MRN" name="region-input-radio-select" type="radio" value="/northern-california/doctors-locations"/>
    <label for="region-code-MRN">California - Northern </label> <br/>
    <input class="radio-button" data-region-id="SCA" id="region-code-SCA" name="region-input-radio-select" type="radio" value="/southern-california/doctors-locations"/>
    <label for="region-code-SCA">California - Southern</label> <br/>
    <input class="radio-button" data-region-id="DB" id="region-code-DB" name="region-input-radio-select" type="radio" value="/colorado-denver-boulder-mountain-northern/doctors-locations"/>
    <label for="region-code-DB">Colorado - Denver / Boulder / Northern / Mountain areas</label> <br/>
    <input class="radio-button" data-region-id="CS" id="region-code-CS" name="region-input-radio-select" type="radio" value="/southern-colorado/doctors-locations"/>
    <label for="region-code-CS">Colorado - Southern </label> <br/>
    <input class="radio-button" data-region-id="GGA" id="region-code-GGA" name="region-input-radio-select" type="radio" value="/georgia/doctors-locations"/>
    <label for="region-code-GGA">Georgia</label> <br/>
    <input class="radio-button" data-region-id="HAW" id="region-code-HAW" name="region-input-radio-select" type="radio" value="/hawaii/doctors-locations"/>
    <label for="region-code-HAW">Hawaii</label> <br/>
    <input class="radio-button" data-region-id="MID" id="region-code-MID" name="region-input-radio-select" type="radio" value="/maryland-virginia-washington-dc/doctors-locations"/>
    <label for="region-code-MID">Maryland / Virginia / Washington, D.C.</label> <br/>
    <input class="radio-button" data-region-id="KNW" id="region-code-KNW" name="region-input-radio-select" type="radio" value="/oregon-washington/doctors-locations"/>
    <label for="region-code-KNW">Oregon / Washington</label> <br/>
    </fieldset>
    </nav>
    </div>
    <div class="modal-buttons ada-buttons-desktop">
    <button class="button -action" id="region-modal-button-cancel">
                Cancel
              </button>
    <button class="button -disabled" disabled="true" id="region-modal-button-continue">
                 Continue
              </button>
    </div>
    <div class="modal-buttons ada-buttons-mobile">
    <button class="button -disabled" disabled="true" id="region-modal-button-continue">
                 Continue
              </button>
    <button class="button -action" id="region-modal-button-cancel">
                Cancel
              </button>
    </div>
    </div>
    </div>
    </div>
    </div>, <div aria-describedby="region-modal-description" aria-labelledby="region-modal-title" class="global-region-modal kp-modal" data-disable-modal="true" data-region-modal-container="" id="global-region-modal-id" lang="en-US" role="dialog">
    <div class="modal-fade-screen">
    <div class="modal-inner" role="document" tabindex="-1">
    <button class="-close" id="global-region-modal-close">
    <span class="screenreader-only">close regional modal</span>
    </button>
    <header class="modal-header">
    <h2 id="region-modal-title" tabindex="0">Choose your region</h2>
    </header>
    <div class="modal-content" id="region-modal-description">
    <p>Select your region from the list below.</p>
    <nav class="region-select-radio-options" data-analytics-location="region-picker-modal">
    <fieldset>
    <legend>Regions</legend>
    <input class="radio-button" data-region-id="MRN" id="region-code-MRN" name="region-input-radio-select" type="radio" value="/northern-california/doctors-locations"/>
    <label for="region-code-MRN">California - Northern </label> <br/>
    <input class="radio-button" data-region-id="SCA" id="region-code-SCA" name="region-input-radio-select" type="radio" value="/southern-california/doctors-locations"/>
    <label for="region-code-SCA">California - Southern</label> <br/>
    <input class="radio-button" data-region-id="DB" id="region-code-DB" name="region-input-radio-select" type="radio" value="/colorado-denver-boulder-mountain-northern/doctors-locations"/>
    <label for="region-code-DB">Colorado - Denver / Boulder / Northern / Mountain areas</label> <br/>
    <input class="radio-button" data-region-id="CS" id="region-code-CS" name="region-input-radio-select" type="radio" value="/southern-colorado/doctors-locations"/>
    <label for="region-code-CS">Colorado - Southern </label> <br/>
    <input class="radio-button" data-region-id="GGA" id="region-code-GGA" name="region-input-radio-select" type="radio" value="/georgia/doctors-locations"/>
    <label for="region-code-GGA">Georgia</label> <br/>
    <input class="radio-button" data-region-id="HAW" id="region-code-HAW" name="region-input-radio-select" type="radio" value="/hawaii/doctors-locations"/>
    <label for="region-code-HAW">Hawaii</label> <br/>
    <input class="radio-button" data-region-id="MID" id="region-code-MID" name="region-input-radio-select" type="radio" value="/maryland-virginia-washington-dc/doctors-locations"/>
    <label for="region-code-MID">Maryland / Virginia / Washington, D.C.</label> <br/>
    <input class="radio-button" data-region-id="KNW" id="region-code-KNW" name="region-input-radio-select" type="radio" value="/oregon-washington/doctors-locations"/>
    <label for="region-code-KNW">Oregon / Washington</label> <br/>
    </fieldset>
    </nav>
    </div>
    <div class="modal-buttons ada-buttons-desktop">
    <button class="button -action" id="region-modal-button-cancel">
                Cancel
              </button>
    <button class="button -disabled" disabled="true" id="region-modal-button-continue">
                 Continue
              </button>
    </div>
    <div class="modal-buttons ada-buttons-mobile">
    <button class="button -disabled" disabled="true" id="region-modal-button-continue">
                 Continue
              </button>
    <button class="button -action" id="region-modal-button-cancel">
                Cancel
              </button>
    </div>
    </div>
    </div>
    </div>, <div class="modal-fade-screen">
    <div class="modal-inner" role="document" tabindex="-1">
    <button class="-close" id="global-region-modal-close">
    <span class="screenreader-only">close regional modal</span>
    </button>
    <header class="modal-header">
    <h2 id="region-modal-title" tabindex="0">Choose your region</h2>
    </header>
    <div class="modal-content" id="region-modal-description">
    <p>Select your region from the list below.</p>
    <nav class="region-select-radio-options" data-analytics-location="region-picker-modal">
    <fieldset>
    <legend>Regions</legend>
    <input class="radio-button" data-region-id="MRN" id="region-code-MRN" name="region-input-radio-select" type="radio" value="/northern-california/doctors-locations"/>
    <label for="region-code-MRN">California - Northern </label> <br/>
    <input class="radio-button" data-region-id="SCA" id="region-code-SCA" name="region-input-radio-select" type="radio" value="/southern-california/doctors-locations"/>
    <label for="region-code-SCA">California - Southern</label> <br/>
    <input class="radio-button" data-region-id="DB" id="region-code-DB" name="region-input-radio-select" type="radio" value="/colorado-denver-boulder-mountain-northern/doctors-locations"/>
    <label for="region-code-DB">Colorado - Denver / Boulder / Northern / Mountain areas</label> <br/>
    <input class="radio-button" data-region-id="CS" id="region-code-CS" name="region-input-radio-select" type="radio" value="/southern-colorado/doctors-locations"/>
    <label for="region-code-CS">Colorado - Southern </label> <br/>
    <input class="radio-button" data-region-id="GGA" id="region-code-GGA" name="region-input-radio-select" type="radio" value="/georgia/doctors-locations"/>
    <label for="region-code-GGA">Georgia</label> <br/>
    <input class="radio-button" data-region-id="HAW" id="region-code-HAW" name="region-input-radio-select" type="radio" value="/hawaii/doctors-locations"/>
    <label for="region-code-HAW">Hawaii</label> <br/>
    <input class="radio-button" data-region-id="MID" id="region-code-MID" name="region-input-radio-select" type="radio" value="/maryland-virginia-washington-dc/doctors-locations"/>
    <label for="region-code-MID">Maryland / Virginia / Washington, D.C.</label> <br/>
    <input class="radio-button" data-region-id="KNW" id="region-code-KNW" name="region-input-radio-select" type="radio" value="/oregon-washington/doctors-locations"/>
    <label for="region-code-KNW">Oregon / Washington</label> <br/>
    </fieldset>
    </nav>
    </div>
    <div class="modal-buttons ada-buttons-desktop">
    <button class="button -action" id="region-modal-button-cancel">
                Cancel
              </button>
    <button class="button -disabled" disabled="true" id="region-modal-button-continue">
                 Continue
              </button>
    </div>
    <div class="modal-buttons ada-buttons-mobile">
    <button class="button -disabled" disabled="true" id="region-modal-button-continue">
                 Continue
              </button>
    <button class="button -action" id="region-modal-button-cancel">
                Cancel
              </button>
    </div>
    </div>
    </div>, <div class="modal-inner" role="document" tabindex="-1">
    <button class="-close" id="global-region-modal-close">
    <span class="screenreader-only">close regional modal</span>
    </button>
    <header class="modal-header">
    <h2 id="region-modal-title" tabindex="0">Choose your region</h2>
    </header>
    <div class="modal-content" id="region-modal-description">
    <p>Select your region from the list below.</p>
    <nav class="region-select-radio-options" data-analytics-location="region-picker-modal">
    <fieldset>
    <legend>Regions</legend>
    <input class="radio-button" data-region-id="MRN" id="region-code-MRN" name="region-input-radio-select" type="radio" value="/northern-california/doctors-locations"/>
    <label for="region-code-MRN">California - Northern </label> <br/>
    <input class="radio-button" data-region-id="SCA" id="region-code-SCA" name="region-input-radio-select" type="radio" value="/southern-california/doctors-locations"/>
    <label for="region-code-SCA">California - Southern</label> <br/>
    <input class="radio-button" data-region-id="DB" id="region-code-DB" name="region-input-radio-select" type="radio" value="/colorado-denver-boulder-mountain-northern/doctors-locations"/>
    <label for="region-code-DB">Colorado - Denver / Boulder / Northern / Mountain areas</label> <br/>
    <input class="radio-button" data-region-id="CS" id="region-code-CS" name="region-input-radio-select" type="radio" value="/southern-colorado/doctors-locations"/>
    <label for="region-code-CS">Colorado - Southern </label> <br/>
    <input class="radio-button" data-region-id="GGA" id="region-code-GGA" name="region-input-radio-select" type="radio" value="/georgia/doctors-locations"/>
    <label for="region-code-GGA">Georgia</label> <br/>
    <input class="radio-button" data-region-id="HAW" id="region-code-HAW" name="region-input-radio-select" type="radio" value="/hawaii/doctors-locations"/>
    <label for="region-code-HAW">Hawaii</label> <br/>
    <input class="radio-button" data-region-id="MID" id="region-code-MID" name="region-input-radio-select" type="radio" value="/maryland-virginia-washington-dc/doctors-locations"/>
    <label for="region-code-MID">Maryland / Virginia / Washington, D.C.</label> <br/>
    <input class="radio-button" data-region-id="KNW" id="region-code-KNW" name="region-input-radio-select" type="radio" value="/oregon-washington/doctors-locations"/>
    <label for="region-code-KNW">Oregon / Washington</label> <br/>
    </fieldset>
    </nav>
    </div>
    <div class="modal-buttons ada-buttons-desktop">
    <button class="button -action" id="region-modal-button-cancel">
                Cancel
              </button>
    <button class="button -disabled" disabled="true" id="region-modal-button-continue">
                 Continue
              </button>
    </div>
    <div class="modal-buttons ada-buttons-mobile">
    <button class="button -disabled" disabled="true" id="region-modal-button-continue">
                 Continue
              </button>
    <button class="button -action" id="region-modal-button-cancel">
                Cancel
              </button>
    </div>
    </div>, <div class="modal-content" id="region-modal-description">
    <p>Select your region from the list below.</p>
    <nav class="region-select-radio-options" data-analytics-location="region-picker-modal">
    <fieldset>
    <legend>Regions</legend>
    <input class="radio-button" data-region-id="MRN" id="region-code-MRN" name="region-input-radio-select" type="radio" value="/northern-california/doctors-locations"/>
    <label for="region-code-MRN">California - Northern </label> <br/>
    <input class="radio-button" data-region-id="SCA" id="region-code-SCA" name="region-input-radio-select" type="radio" value="/southern-california/doctors-locations"/>
    <label for="region-code-SCA">California - Southern</label> <br/>
    <input class="radio-button" data-region-id="DB" id="region-code-DB" name="region-input-radio-select" type="radio" value="/colorado-denver-boulder-mountain-northern/doctors-locations"/>
    <label for="region-code-DB">Colorado - Denver / Boulder / Northern / Mountain areas</label> <br/>
    <input class="radio-button" data-region-id="CS" id="region-code-CS" name="region-input-radio-select" type="radio" value="/southern-colorado/doctors-locations"/>
    <label for="region-code-CS">Colorado - Southern </label> <br/>
    <input class="radio-button" data-region-id="GGA" id="region-code-GGA" name="region-input-radio-select" type="radio" value="/georgia/doctors-locations"/>
    <label for="region-code-GGA">Georgia</label> <br/>
    <input class="radio-button" data-region-id="HAW" id="region-code-HAW" name="region-input-radio-select" type="radio" value="/hawaii/doctors-locations"/>
    <label for="region-code-HAW">Hawaii</label> <br/>
    <input class="radio-button" data-region-id="MID" id="region-code-MID" name="region-input-radio-select" type="radio" value="/maryland-virginia-washington-dc/doctors-locations"/>
    <label for="region-code-MID">Maryland / Virginia / Washington, D.C.</label> <br/>
    <input class="radio-button" data-region-id="KNW" id="region-code-KNW" name="region-input-radio-select" type="radio" value="/oregon-washington/doctors-locations"/>
    <label for="region-code-KNW">Oregon / Washington</label> <br/>
    </fieldset>
    </nav>
    </div>, <div class="modal-buttons ada-buttons-desktop">
    <button class="button -action" id="region-modal-button-cancel">
                Cancel
              </button>
    <button class="button -disabled" disabled="true" id="region-modal-button-continue">
                 Continue
              </button>
    </div>, <div class="modal-buttons ada-buttons-mobile">
    <button class="button -disabled" disabled="true" id="region-modal-button-continue">
                 Continue
              </button>
    <button class="button -action" id="region-modal-button-cancel">
                Cancel
              </button>
    </div>, <div class="cloudservice testandtarget"><script type="text/javascript">
        CQ_Analytics.TestTarget.maxProfileParams = 11;
    
        if (CQ_Analytics.CCM) {
            if (CQ_Analytics.CCM.areStoresInitialized) {
                CQ_Analytics.TestTarget.registerMboxUpdateCalls();
            } else {
                CQ_Analytics.CCM.addListener("storesinitialize", function (e) {
                    CQ_Analytics.TestTarget.registerMboxUpdateCalls();
                });
            }
        } else {
            // client context not there, still register calls
            CQ_Analytics.TestTarget.registerMboxUpdateCalls();
        }
        </script>
    </div>]



```python
 
 
 
```


```python
 
```


```python
 
```

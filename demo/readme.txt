Entity centric demo
===================
Analysis on "events" has limits. Sometimes you need to examine behaviours of entities
over multiple events.

Background
===========
This demo accompanies the "Entity-centric indexing" talk from Elastic{on} 2015 and
uses some anonymized real-world data to build profiles of buyer behaviours based
on their behaviour in the Amazon marketplace.
The talk provides useful background and a recording is here: https://www.youtube.com/watch?v=yBf7oeJKH2Y

UPDATE - 20th June 2018
This version has been adapted to use the new Painless scripting language and has been 
tested with elasticsearch version 6.3.0

Loading the data, building entities
====================================
1) Run the script "loadEvent.sh". This will drop then create the "anonreviews" events index
2) Run the script "registerUpdateScript.sh". This installs the script used for updating a 
   reviewer with their latest reviews
3) Run the script "buildEntities.sh" to pull the review events sorted by reviewerId and 
time from the "anonreviews" index and it will create "reviewer" documents in a "reviewers" index.

Step 3 relies on 2 scripts 
1) ESEntityCentricIndexing.py - generic script to pull data from
an event-centric index and push to an entity-centric one.
2) ReviewerProfileUpdater.painless - our domain-specific business logic for summarising reviewer behaviour

Interesting query
===================
//Find the seller who has more than their fair-share of "fanboy" reviewers..
POST reviewers/_search
{
    "query": {
        "match": {
            "profile": "fanboy"
        }
    },
    "aggs": {
        "keywords": {
            "significant_terms": {
                "field": "vendors.vendorId"
            }
        }
    }
}

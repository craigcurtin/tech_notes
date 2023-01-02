
https://dev.startree.ai/docs/pinot/demo-apps/pizza-shop
https://dev.startree.ai/docs/pinot/getting-started/



https://github.com/mneedham/real-time-analytics-book


docker-compose \
  -f docker-compose-base.yml \
  -f docker-compose-pinot-m1.yml \
  -f docker-compose-dashboard.yml \
  -f docker-compose-enrich-streams.yml \
  -f docker-compose-dashboard-enriched.yml \
  up

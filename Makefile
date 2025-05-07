.PHONY: dev backend frontend

dev:
	@echo "🔧 Iniciando backend y frontend en terminales separadas..."
	@osascript -e 'tell application "Terminal" to do script "cd $(PWD)/backend && source venv/bin/activate && uvicorn app.main:app --reload"'
	@sleep 2
	@osascript -e 'tell application "Terminal" to do script "cd $(PWD)/frontend && npm run dev"'

backend:
	cd backend && source venv/bin/activate && uvicorn app.main:app --reload

frontend:
	cd frontend && npm run dev

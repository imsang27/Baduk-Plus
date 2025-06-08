class BadukBoard {
    constructor(containerId, size = 19) {
        this.container = document.getElementById(containerId);
        this.size = size;
        this.board = Array(size).fill().map(() => Array(size).fill(null));
        this.currentMove = 0;
        this.moves = [];
        this.initialize();
    }

    initialize() {
        this.createBoard();
        this.drawGrid();
    }

    createBoard() {
        this.container.style.position = 'relative';
        this.container.style.width = '100%';
        this.container.style.height = '100%';
        this.container.style.background = '#DEB887';
    }

    drawGrid() {
        const canvas = document.createElement('canvas');
        canvas.style.width = '100%';
        canvas.style.height = '100%';
        this.container.appendChild(canvas);
        this.canvas = canvas;
        this.ctx = canvas.getContext('2d');

        // 캔버스 크기 설정
        const resizeCanvas = () => {
            const rect = this.container.getBoundingClientRect();
            canvas.width = rect.width;
            canvas.height = rect.height;
            this.drawGrid();
        };

        window.addEventListener('resize', resizeCanvas);
        resizeCanvas();
    }

    drawGrid() {
        const ctx = this.ctx;
        const width = this.canvas.width;
        const height = this.canvas.height;
        const cellSize = Math.min(width, height) / (this.size + 1);

        ctx.clearRect(0, 0, width, height);
        ctx.strokeStyle = '#000';
        ctx.lineWidth = 1;

        // 수평선
        for (let i = 0; i < this.size; i++) {
            ctx.beginPath();
            ctx.moveTo(cellSize, cellSize * (i + 1));
            ctx.lineTo(cellSize * this.size, cellSize * (i + 1));
            ctx.stroke();
        }

        // 수직선
        for (let i = 0; i < this.size; i++) {
            ctx.beginPath();
            ctx.moveTo(cellSize * (i + 1), cellSize);
            ctx.lineTo(cellSize * (i + 1), cellSize * this.size);
            ctx.stroke();
        }

        // 별점
        const starPoints = this.getStarPoints();
        starPoints.forEach(point => {
            ctx.beginPath();
            ctx.arc(
                cellSize * (point.x + 1),
                cellSize * (point.y + 1),
                cellSize * 0.1,
                0,
                Math.PI * 2
            );
            ctx.fillStyle = '#000';
            ctx.fill();
        });
    }

    getStarPoints() {
        if (this.size === 19) {
            return [
                {x: 3, y: 3}, {x: 3, y: 9}, {x: 3, y: 15},
                {x: 9, y: 3}, {x: 9, y: 9}, {x: 9, y: 15},
                {x: 15, y: 3}, {x: 15, y: 9}, {x: 15, y: 15}
            ];
        }
        return [];
    }

    placeStone(x, y, color) {
        if (x < 0 || x >= this.size || y < 0 || y >= this.size) return false;
        if (this.board[y][x] !== null) return false;

        this.board[y][x] = color;
        this.drawStone(x, y, color);
        this.moves.push({x, y, color});
        this.currentMove++;
        return true;
    }

    drawStone(x, y, color) {
        const ctx = this.ctx;
        const cellSize = Math.min(this.canvas.width, this.canvas.height) / (this.size + 1);
        const centerX = cellSize * (x + 1);
        const centerY = cellSize * (y + 1);
        const radius = cellSize * 0.45;

        ctx.beginPath();
        ctx.arc(centerX, centerY, radius, 0, Math.PI * 2);
        ctx.fillStyle = color === 'black' ? '#000' : '#fff';
        ctx.fill();
        ctx.strokeStyle = '#000';
        ctx.lineWidth = 1;
        ctx.stroke();
    }

    updateFromGameData(gameData) {
        if (!gameData.수순) return;

        // 보드 초기화
        this.board = Array(this.size).fill().map(() => Array(this.size).fill(null));
        this.moves = [];
        this.currentMove = 0;

        // 수순 데이터로부터 돌 배치
        Object.entries(gameData.수순).forEach(([moveNumber, move]) => {
            const color = moveNumber % 2 === 0 ? 'black' : 'white';
            this.placeStone(move.x, move.y, color);
        });
    }
}